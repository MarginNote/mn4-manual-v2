# pipeline —— `src/` 规范化（进入 SSG 之前）

把 `src/`（wolai 导出的 Markdown + 媒体）规范化、压缩为 `build/src/`，作为交给静态站点
生成器（SSG）阶段的交接物。与具体 SSG **无关**——只产出干净的 Markdown + 压缩媒体。

> 本包不单独运行；构建入口与命令在仓库根 `dodo.py`（见根 [`README`](../README.md)）。

## 模块

| 模块 | 职责 |
|---|---|
| `assets` | 共享契约：资源识别 / 分类 / 16 位 path-hash 命名（纯路径逻辑，无重依赖） |
| `format_page` | `render_page(md, out, published, id2slug)` —— 遍历 mistletoe 语法树转换**一页**（含站内链接 id→slug 改写） |
| `format_media` | `encode(src, dst, kind)` —— ffmpeg 编码**一个文件** |
| `__init__` | 发布集 + slug 映射加载 + doit 任务 `task_page` / `task_page_en` / `task_media`（由 `dodo.py` 导入） |

`format_page` / `format_media` 各自只处理一页 / 一个文件，对称、易测；`assets` 保证
「正文引用名 / 磁盘文件名 / doit 构建目标」三者一致。

## 内容转换（遍历语法树，绝不正则解析 Markdown）

1. **章节规范化**：保留首个标题为 `h1`；正文标题按祖先栈重排为连续不跳级的层级（从 `h2`
   起）。既把 wolai 的多个 `#` 章节降为 `h2`，也把缺上级的 `###`（无 `h2`）升级为 `h3`。
2. **跨页链接**（纯 id）：`wolai.com/<id>` 与根相对 `/<id>`；发布集（`toc.yaml`）内 →
   站内相对链接 `../<slug>/index.md`（slug 来自 toc，去深锚）；自链接 / 悬空 → 降级为纯文本；外链原样保留。
3. **媒体引用**：改写为压缩产物的哈希名；gif 与视频统一为**动画 WebP**（仍是 `<img>`，浏览器
   原生循环播放、图片灯箱 glightbox 天然覆盖，不再产出 `<video>`）；引用但磁盘缺失的图 →
   降级（去掉图片、保留 alt 文本）。

## 媒体压缩（ffmpeg）

| 源 | 产物 | 参数 | 正文呈现 |
|---|---|---|---|
| png / jpg / jpeg | webp（静态） | q80, ≤1200px, lanczos | `<img>` |
| gif | webp（动画） | libwebp_anim, loop 0, q60, ≤1200px, 帧率 ≤12 保留否则降 10 | `<img>` |
| mp4 / mov / webm / m4v | webp（动画） | 同上（KISS：一律转动图，无 `<video>`） | `<img>` |
| 其它（.ttf…） | 原样复制 | — | 链接 |

源目录 `src/` 始终保留未压缩原件，只有 `build/` 内是压缩产物（动图 webp 体积换取无 `<video>`
的简洁；实测约 2GB → 约 312MB）。

## 命名：16 位 path-hash

`build/` 内资源名 = `md5(源相对路径)[:16] + 新后缀`（源路径 = `<id>/<子目录>/<原名>`）。由
**源路径**决定（非文件内容、与 slug/语言无关）→ 确定、增量安全、跨语言共用同一份；纯 ASCII
免编码、定长无冲突，并抹掉原文件名里的拍摄元数据。产物按 **slug** 目录归置（见下）。`src/` 保留原始可读名。

## 输出与交接

```
build/src/<slug>/         # 目录名 = toc.yaml 的英文 slug（中英共用）
  index.md                # 中文规范化正文（默认语言）
  index.en.md             # 英文译文（若 i18n/en/<id>/index.md 存在；mkdocs-static-i18n suffix 结构）
  image/ video/ file/     # 该页被引用到的压缩资源（哈希名；中英共用单份）
```

`task_page_en` 把 `i18n/en/<id>/index.md` 落到 `build/src/<slug>/index.en.md`（并改写站内链接
id→slug）。`toc.yaml` / `glossary.md` / `synonyms.yaml` / `faq.yaml` **不**进 `build/src`——它们是
下游输入（toc→导航/ slug、glossary→翻译参照、faq→FAQ 页、synonyms→搜索），使 `build/src`
只含「编译后的页面 + 资源」。
