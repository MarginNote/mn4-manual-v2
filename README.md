# MarginNote 4 用户手册

MN4 用户手册：内容源是 wolai 导出的 Markdown（见 `src/`），经构建管线规范化、压缩，再由
mkdocs 渲染为可部署的静态站点。

## 结构

```
src/              中文内容源：每页一个 wolai-id 目录 + toc.yaml（结构/元数据，含 slug）
                  + glossary.md（中英术语表，wolai 导出）+ synonyms.yaml/faq.yaml（见 src/README.md）
i18n/en/          英文版源（自包含）：每页 <id>/index.md 译文 + toc.yaml（目录英文 overlay）
config.py         路径布局（可被环境变量覆盖；pipeline 与 ssg 共用）
pipeline/         内容规范化 + 媒体压缩 → build/src（详见 pipeline/README.md）
ssg/              build/src → build/site，mkdocs + Material + static-i18n + Pagefind（详见 ssg/README.md）
dodo.py           doit 构建入口（page → page_en → media → config → home → site → search）
requirements.txt  构建依赖（另需系统 ffmpeg）
```

站点特性（与旧站对齐）：**中英双语**（中文默认在根路径，英文在 `/en/`，由 mkdocs-static-i18n
以 suffix 结构生成）、**英文 slug URL**（页面目录名）、品牌色 `#219cfb`、深/浅色切换、
首页 hero + 难度·阅读时长卡片、Pagefind 中英搜索、图片点击放大（glightbox）。均为服务端
渲染——除搜索（静态站搜索必需）与图片放大外不依赖 JS，无 SPA。

## 构建

```bash
virtualenv .venv
.venv/bin/pip install -r requirements.txt    # 另需系统 ffmpeg / ffprobe
.venv/bin/doit -n 2                           # 全链路 src/ → build/site/
```

生成物都在 `build/` 下（已 gitignore）：`build/src` 规范化产物、`build/site` 站点（含
`build/site/pagefind/` 搜索索引）、`build/mkdocs.yml`、`build/overrides` 主题覆盖。

> 增量仅按输入文件时间戳/哈希失效，**不跟踪转换代码/配置变化**：改了 `ssg/` 或
> `pipeline/` 的代码后，自行 `doit forget <任务>` 或 `doit clean` 再构建（CI 一律全新构建）。

## i18n（中英双语）

- 中文为默认语言（根路径 `/`），英文在 `/en/`；URL 用英文 **slug**（`toc.yaml` 每页 `slug` 字段，
  中英共用同一目录名）。
- 英文版源**自包含**于 `i18n/en/`：每页 `i18n/en/<id>/index.md`（与 `src/<id>/` 平行，预留
  `image/` 以便日后译图）+ `i18n/en/toc.yaml`（目录英文文案 overlay，按中文名/ id 作键）。
- `src/toc.yaml` 保持**纯中文 + slug**；构建期 ssg 把英文 overlay **内存合并**（`load_merged_toc`），
  两个源文件都不被改写。
- **媒体单份存放、中英共用**：static-i18n 自动把 `/en/` 页面的相对引用回指根目录，无副本。
- 翻译术语一致性参照 `src/glossary.md`（中英术语表，wolai 导出，保持原样不结构化）。

## 部署

纯静态：`build/site/` 可托管在任意静态服务。默认发布在子路径前缀 `/mn4` 下，可经环境变量覆盖：

| 变量 | 默认 | 说明 |
|---|---|---|
| `MN_URL_PREFIX` | `/mn4` | 站点子路径前缀（`""` = 根路径） |
| `MN_SITE_HOST` | `https://manual.marginnote.com.cn` | 站点主机 |
| `MN_SITE_URL` | `<host><prefix>/` | 完整 URL；给定则覆盖上两者 |

默认 `site_url` = `https://manual.marginnote.com.cn/mn4/`（生产域名）。资源引用均为相对路径
（按页面深度改写），故在任意前缀/域名下都正确。

### GitHub Pages（CI）

`.github/workflows/deploy.yml`：push 到 `main` 即构建（装 ffmpeg → `doit` 全新构建 → Pagefind
索引）并发布到 GitHub Pages（仓库 Settings → Pages → Source 选 **GitHub Actions**）。

> GitHub Pages 项目站点路径 = **仓库名**，故工作流经 `MN_SITE_URL` 覆盖为本仓库实际地址
> **`https://marginnote.github.io/mn4-manual-v2/`**；生产部署用默认的 `manual.marginnote.com.cn/mn4/`。

## 文档

- 撰写 / 增改页面：[`src/README.md`](src/README.md)
- 内容管线：[`pipeline/README.md`](pipeline/README.md)
- 站点生成（SSG）：[`ssg/README.md`](ssg/README.md)
