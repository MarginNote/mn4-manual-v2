# MarginNote 4 用户手册

MN4 用户手册：内容源是 wolai 导出的 Markdown（见 `src/`），经构建管线规范化、压缩，再由
mkdocs 渲染为可部署的静态站点。

## 结构

```
src/              内容源：每页一个 wolai-id 目录 + toc.yaml/synonyms.yaml/faq.yaml（撰写见 src/README.md）
config.py         路径布局（可被环境变量覆盖；pipeline 与 ssg 共用）
pipeline/         内容规范化 + 媒体压缩 → build/src（详见 pipeline/README.md）
ssg/              build/src → build/site，mkdocs + Material + Pagefind（详见 ssg/README.md）
dodo.py           doit 构建入口（page → media → config → home → site → search）
requirements.txt  构建依赖（另需系统 ffmpeg）
```

站点特性（与旧站对齐）：品牌色 `#219cfb`、深/浅色切换、首页 hero + 难度·阅读时长卡片、
Pagefind 中文搜索、图片点击放大（glightbox）、上一篇/下一篇。均为服务端渲染——除搜索
（静态站搜索必需）与图片放大外不依赖 JS，无 SPA。

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

## 文档

- 撰写 / 增改页面：[`src/README.md`](src/README.md)
- 内容管线：[`pipeline/README.md`](pipeline/README.md)
- 站点生成（SSG）：[`ssg/README.md`](ssg/README.md)
