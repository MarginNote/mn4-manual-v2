# ssg —— 站点生成（mkdocs + Material + Pagefind）：`build/src` → `build/site`

把规范化产物 `build/src` 渲染成可部署站点。与内容管线**解耦、同一 doit 编排**，以 `build/src`
为交接契约；整包可替换以更换 SSG。mkdocs 以子进程调用，构建后再跑 Pagefind 建中文搜索索引；
本包只生成配置、派生页面与静态资源。路径布局来自顶层 `config.py`（**不 import pipeline**）。

> 本包不单独运行；构建入口与命令在仓库根 `dodo.py`（见根 [`README`](../README.md)）。

## 模块

| 模块 | 职责 |
|---|---|
| `config` | 从 `toc.yaml`(+ `i18n/en/toc.yaml`) 生成 `build/mkdocs.yml`（Material + 品牌 + 导航 + **mkdocs-static-i18n** + 搜索接线）。`load_merged_toc()` 内存合并中英目录；`write_mkdocs_yml()` |
| `pages` | 生成中英双语首页 `index.md` / `index.en.md`（hero + 分区卡片）；标题/缩略图从各页规范化 md 经 **mistletoe AST** 读取（不正则解析）：`build_home()` / `write_home()` |
| `__init__` | doit 任务 `task_config` / `task_home` / `task_site` / `task_search`（由 `dodo.py` 导入）；`task_config` 还负责把下方手维护资源拷进 `build/` |

## 手维护资源（构建期由 `config` 任务拷进 `build/`）

| 文件 | 内容 |
|---|---|
| `static/stylesheets/extra.css` | 品牌色 `#219cfb`、随主题切换的头部/页脚、全宽、首页 hero/卡片、Pagefind 模态样式 |
| `static/javascripts/pagefind-init.js` | 初始化 Pagefind UI；复用 Material `#__search` 开关（无 SPA / 无自定义模态 JS） |
| `static/mn4-logo.png` | 站点 logo / favicon |
| `overrides/partials/header.html` | 覆盖 Material 头部：搜索按钮 + 跨站链接 + 语言切换；自定义文案随 `is_en` 切中/英（对照 pin 的上游版本同步） |
| `overrides/partials/search.html` | 头部搜索框换成 Pagefind 容器（纯 CSS 显隐，挂在 Material 模态外壳上） |

## 生成物（都在 `build/` 下）

| 任务 | 产物 |
|---|---|
| `config` | `build/mkdocs.yml`（主题 + 品牌 + 导航 + i18n + 搜索接线）+ 拷贝 `static/`（css/js/logo）→ `build/src/`、`overrides/` → `build/overrides/` |
| `home` | `build/src/index.md` + `index.en.md`（中英 hero + 卡片） |
| `site` | `build/site/`（`mkdocs build` 输出；中文在根、英文在 `/en/`） |
| `search` | `build/site/pagefind/`（Pagefind 中英搜索索引，按页 `<html lang>` 自动分两套） |

`mkdocs.yml` 生成到 `build/`，故其 `docs_dir: src` / `site_dir: site` / `custom_dir: overrides`
相对 `build/` 解析（→ `build/src` / `build/site` / `build/overrides`）。

## 导航与 i18n

`mkdocs.yml` 的 `nav` 由 `toc.yaml`（section → category → pages）派生，页面路径用 **slug** 目录；
**页面标题取自各页 H1**（中/英各自的 H1，天然双语，不在 nav 里重复维护）。分区/分类的**组标题**
经 mkdocs-static-i18n 的 `nav_translations`（标题字符串映射，由 `i18n/en/toc.yaml` 自动生成）译为英文。

英文版走 static-i18n 的 **suffix 结构**：中文为默认语言（根路径），英文 `index.en.md` → `/en/`。
`site_name` / `site_description` / `copyright` 按语言覆盖；媒体单份存放，`/en/` 页面的相对引用由
static-i18n 自动回指根目录（**无副本**）。首页卡片的难度/阅读时长取自 `toc.yaml`，英文描述取自
`i18n/en/toc.yaml`（构建期 `load_merged_toc()` 内存合并，不改动 `toc.yaml`）。

## 搜索

Material 内置搜索（jieba，中文分词较弱）**已禁用**，改用 **Pagefind**（extended 含 CJK 分词；
构建后在 `build/site` 上建索引）。Pagefind 按每页 `<html lang>` **自动分中/英两套索引**。头部搜索框
经 `custom_dir` 覆盖接入 Pagefind UI，复用 Material 原生模态开关——除 Pagefind 自身外不引入额外前端框架。

## 现状

中英双语（中文默认 / 英文 `/en/`）、slug URL、首页 hero+卡片、品牌色、随系统深/浅色
（头部/页脚自适应）、全宽、Pagefind 中英搜索、图片放大（glightbox）均已就绪。FAQ
（`src/faq.yaml`）、同义词查询扩展（`src/synonyms.yaml`）规划见 [`REWRITE_PLAN.md`](../REWRITE_PLAN.md)。
