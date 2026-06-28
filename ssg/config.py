"""从 toc.yaml 生成 mkdocs.yml（主题 + 导航）。

配置即代码：改主题 / 扩展 / 插件在本文件编辑；导航由 toc.yaml 派生。
页面标题不写进 nav —— 让 mkdocs 从各页 H1 自动取，避免与 toc 注释里的标题二次维护。

路径来自顶层 config.py（不 import pipeline）。mkdocs.yml 生成到 build/，故其 docs_dir /
site_dir 用相对 build/ 的 "src" / "site"（mkdocs 按配置文件所在目录解析相对路径）。
"""

import yaml

from config import BUILD_SRC, SITE, MKDOCS_YML, TOC  # noqa: F401  (SITE/MKDOCS_YML 供 ssg 包用)

DOCS = BUILD_SRC                 # mkdocs docs_dir = build/src


def _nav(toc) -> list:
    """toc.yaml（section → category → pages）→ mkdocs nav（含首页）。"""
    nav: list = [{"首页": "index.md"}]
    for section in toc or []:
        cats = []
        for cat in (section or {}).get("categories", []) or []:
            pages = [f"{pg['id']}/index.md"
                     for pg in (cat or {}).get("pages", []) or [] if pg.get("id")]
            if pages:
                cats.append({cat.get("category", "?"): pages})
        if cats:
            nav.append({section.get("section") or section.get("title") or "?": cats})
    return nav


def mkdocs_config(toc) -> dict:
    return {
        "site_name": "MarginNote 4 用户手册",
        "docs_dir": "src",       # 相对 build/mkdocs.yml → build/src
        "site_dir": "site",      # → build/site
        "use_directory_urls": True,
        "theme": {
            "name": "material",
            "language": "zh",
            # 旧站品牌色 ~#219cfb，后续可换自定义 palette
            "palette": {"primary": "light blue", "accent": "light blue"},
            "features": [
                "navigation.sections", "navigation.top", "toc.follow",
                "content.code.copy", "search.suggest", "search.highlight",
            ],
        },
        "plugins": ["search"],   # Material 内置搜索（中文分词较弱；CJK 方案见 REWRITE_PLAN）
        "markdown_extensions": [
            "tables", "attr_list", "md_in_html", "admonition", "footnotes",
            {"toc": {"permalink": True}},
            "pymdownx.superfences", "pymdownx.details",
        ],
        "nav": _nav(toc),
    }


def write_mkdocs_yml() -> None:
    toc = yaml.safe_load(TOC.read_text(encoding="utf-8")) or []
    MKDOCS_YML.parent.mkdir(parents=True, exist_ok=True)
    MKDOCS_YML.write_text(
        yaml.safe_dump(mkdocs_config(toc), allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
