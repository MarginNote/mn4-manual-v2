# ssg —— 站点生成（mkdocs + Material）：`build/src` → `build/site`

把规范化产物 `build/src` 渲染成可部署站点。与内容管线**解耦、同一 doit 编排**，以 `build/src`
为交接契约；整包可替换以更换 SSG。mkdocs 以子进程调用，本包只生成它
的配置与派生页面。路径布局来自顶层 `config.py`（**不 import pipeline**）。

> 本包不单独运行；构建入口与命令在仓库根 `dodo.py`（见根 [`README`](../README.md)）。

## 模块

| 模块 | 职责 |
|---|---|
| `config` | 从 `toc.yaml` 生成 `build/mkdocs.yml`（Material 主题 + 导航）：`mkdocs_config()` / `write_mkdocs_yml()` |
| `pages` | 生成派生页面：`write_home()`（首页，当前为占位） |
| `__init__` | doit 任务 `task_config` / `task_site`（由 `dodo.py` 导入） |

## 生成物（都在 `build/` 下）

| 任务 | 产物 |
|---|---|
| `config` | `build/mkdocs.yml`（主题 + 导航）+ `build/src/index.md`（首页占位） |
| `site` | `build/site/`（`mkdocs build` 输出） |

`mkdocs.yml` 生成到 `build/`，故其 `docs_dir: src` / `site_dir: site` 相对 `build/` 解析
（→ `build/src` / `build/site`）。

## 导航

`mkdocs.yml` 的 `nav` 由 `toc.yaml`（section → category → pages）派生；**页面标题取自各页
H1**，不在 nav 里重复维护。

## 现状

首页为占位；站点搜索暂用 Material 内置（中文分词较弱）。CJK 搜索（Pagefind + 同义词扩展）
/ FAQ / i18n / 品牌色 / 图片缩放等规划见 [`REWRITE_PLAN.md`](../REWRITE_PLAN.md)。
