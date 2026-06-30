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

### 阿里云 OSS（CI，生产）

`.github/workflows/deploy-oss.yml`：push 到 `main` 即构建（装 ffmpeg → `doit` 全新构建 →
Pagefind 索引），再用 `ossutil sync` 把 `build/site/` 同步到 bucket 的 **`mn4/` 前缀**。不覆盖
`MN_SITE_URL`，直接用 `config.py` 默认的生产 URL `https://manual.marginnote.com.cn/mn4/`
（`/mn4` 前缀已烘进产物）。

> **与同 bucket 旧站隔离**：旧 repo 占用 bucket 根的 `/index.html`、`/docs/`、`/mn3/`；本工作流
> 只写 `mn4/` 前缀，`--delete` 也只清理该前缀内的残留对象，**永不触及旧站产物**——故同一 bucket
> 并存无冲突。CDN 刷新同样只针对 `/mn4/` 目录。

部署账号在仓库 / 组织级配置以下 Secrets 与 Variables：

| 名称 | 类型 | 必需 | 说明 |
|---|---|---|---|
| `ACCESS_KEY_ID` | secret | ✅ | OSS 部署账号 AccessKey ID |
| `ACCESS_KEY_SECRET` | secret | ✅ | OSS 部署账号 AccessKey Secret |
| `OSS_BUCKET` | var | ✅ | 目标 Bucket 名 |
| `OSS_ENDPOINT` | var | ✅ | 如 `oss-cn-beijing.aliyuncs.com` |
| `OSS_REGION` | var | ⬜ | 默认从 endpoint 推导（`oss-<region>...`） |
| `CDN_DOMAIN` | var | ⬜ | 设置则刷新 CDN，如 `manual.marginnote.com.cn` |
| `CDN_ACCESS_KEY_ID` | secret | ⬜ | CDN 账号（设了 `CDN_DOMAIN` 时必需） |
| `CDN_ACCESS_KEY_SECRET` | secret | ⬜ | CDN 账号 Secret |

> ossutil v2 默认 sign-version v4 必须显式 region；`--force` 跳过覆盖时的交互提示，否则非首次
> 部署会卡死 CI。CDN 账号通常与 OSS 部署账号不同，故单列。

## 文档

- 撰写 / 增改页面：[`src/README.md`](src/README.md)
- 内容管线：[`pipeline/README.md`](pipeline/README.md)
- 站点生成（SSG）：[`ssg/README.md`](ssg/README.md)
