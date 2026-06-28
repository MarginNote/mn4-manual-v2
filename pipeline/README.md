# pipeline —— `src/` 规范化（进入 SSG 之前）

把 `src/`（wolai 导出的 Markdown + 媒体）规范化、压缩为 `build/src/`，作为交给静态站点
生成器（SSG）阶段的交接物。与具体 SSG **无关**——只产出干净的 Markdown + 压缩媒体。

> 本包不单独运行；构建入口与命令在仓库根 `dodo.py`（见根 [`README`](../README.md)）。

## 模块

| 模块 | 职责 |
|---|---|
| `assets` | 共享契约：资源识别 / 分类 / 16 位 path-hash 命名（纯路径逻辑，无重依赖） |
| `format_page` | `render_page(md, out, published)` —— 遍历 mistletoe 语法树转换**一页** |
| `format_media` | `encode(src, dst, kind)` —— ffmpeg 编码**一个文件** |
| `__init__` | 发布集加载 + doit 任务创建器 `task_page` / `task_media`（由 `dodo.py` 导入） |

`format_page` / `format_media` 各自只处理一页 / 一个文件，对称、易测；`assets` 保证
「正文引用名 / 磁盘文件名 / doit 构建目标」三者一致。

## 内容转换（遍历语法树，绝不正则解析 Markdown）

1. **章节规范化**：保留首个标题为 `h1`；正文标题按祖先栈重排为连续不跳级的层级（从 `h2`
   起）。既把 wolai 的多个 `#` 章节降为 `h2`，也把缺上级的 `###`（无 `h2`）升级为 `h3`。
2. **跨页链接**（纯 id）：`wolai.com/<id>` 与根相对 `/<id>`；发布集（`toc.yaml`）内 →
   站内相对链接 `../<id>/index.md`（去深锚）；自链接 / 悬空 → 降级为纯文本；外链原样保留。
3. **媒体引用**：改写为压缩产物的哈希名；gif/视频改写为 `<video>`；引用但磁盘缺失的图 →
   降级（去掉图片、保留 alt 文本）。

## 媒体压缩（ffmpeg）

| 源 | 产物 | 参数 | 正文呈现 |
|---|---|---|---|
| png / jpg / jpeg | webp | q80, ≤1200px, lanczos | `<img>` |
| gif | mp4 | h264 / yuv420p / faststart, crf28, ≤1200px, 帧率 ≤12 保留否则降 10 | `<video autoplay loop muted playsinline>` |
| mp4 / mov / … | mp4 | h264, crf26, ≤1280px, 帧率封顶 30 | 链接 |
| 其它（.ttf…） | 原样复制 | — | 链接 |

源目录 `src/` 始终保留未压缩原件，只有 `build/` 内是压缩产物（实测约 2.1GB → 84MB）。

## 命名：16 位 path-hash

`build/` 内资源名 = `md5(源相对路径)[:16] + 新后缀`，保留 `<id>/<子目录>/` 层级。由**路径**
决定（非文件内容）→ 确定、增量安全、不耦合正文与媒体内容；纯 ASCII 免编码、定长无冲突，
并抹掉原文件名里的拍摄元数据。`src/` 保留原始可读名。

## 输出与交接

```
build/src/<wolai-id>/
  index.md            # 规范化正文
  image/ video/ file/ # 该页被引用到的压缩资源（哈希名）
```

`toc.yaml` / `synonyms.yaml` / `faq.yaml` **不**进 `build/src`——它们是下游 SSG 阶段的输入
（toc→导航、faq→FAQ 页、synonyms→搜索），由 SSG 阶段直接读 `src/`，使 `build/src` 只含
「编译后的页面 + 资源」。
