"""从 toc.yaml 生成 mkdocs.yml（主题 + 导航 + 品牌 + 搜索接线）。

配置即代码：改主题 / 扩展 / 插件在本文件编辑；导航由 toc.yaml 派生。
页面标题不写进 nav —— 让 mkdocs 从各页 H1 自动取，避免与 toc 注释里的标题二次维护。

路径来自顶层 config.py（不 import pipeline）。mkdocs.yml 生成到 build/，故其 docs_dir /
site_dir / custom_dir 用相对 build/ 的 "src" / "site" / "overrides"（mkdocs 按配置文件
所在目录解析相对路径）。

搜索：Material 内置搜索（jieba，中文分词较弱）已禁用，改用构建后的 Pagefind（CJK 友好）。
头部搜索按钮与模态由 overrides/partials/{header,search}.html 提供，Pagefind 资源经
extra_css / extra_javascript 接入（构建后的 `pagefind` 步骤生成 /pagefind/）。
"""

import yaml

from config import (  # noqa: F401  (部分名字供 ssg 包其它模块复用)
    BUILD_SRC,
    MKDOCS_YML,
    OVERRIDES,
    SITE,
    SITE_DESCRIPTION,
    SITE_URL,
    TOC,
)

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
        "site_url": SITE_URL,
        "site_description": SITE_DESCRIPTION,
        "docs_dir": "src",            # 相对 build/mkdocs.yml → build/src
        "site_dir": "site",           # → build/site
        "use_directory_urls": True,
        "theme": {
            "name": "material",
            "language": "zh",
            "custom_dir": "overrides",  # → build/overrides（Pagefind 头部覆盖）
            "logo": "mn4-logo.png",
            "favicon": "mn4-logo.png",
            "font": False,              # 系统字体：CJK 友好、免加载 Google Fonts、低端设备更快
            # media 查询 → 首访跟随系统深/浅色；toggle 可手动覆盖
            "palette": [
                {"media": "(prefers-color-scheme: light)", "scheme": "default",
                 "toggle": {"icon": "material/weather-night", "name": "切换到深色模式"}},
                {"media": "(prefers-color-scheme: dark)", "scheme": "slate",
                 "toggle": {"icon": "material/weather-sunny", "name": "切换到浅色模式"}},
            ],
            "features": [
                "navigation.sections", "navigation.top",
                "navigation.tracking", "toc.follow",
                "content.code.copy", "content.tooltips",
            ],
        },
        # Material 内置搜索禁用（不在 plugins 列表即关闭）；图片缩放用 glightbox。
        "plugins": ["glightbox"],
        "markdown_extensions": [
            "tables", "attr_list", "md_in_html", "admonition", "footnotes",
            "pymdownx.superfences", "pymdownx.details",
            {"toc": {"permalink": True}},
        ],
        "extra_css": ["stylesheets/extra.css", "/pagefind/pagefind-ui.css"],
        "extra_javascript": ["/pagefind/pagefind-ui.js", "javascripts/pagefind-init.js"],
        # 跨站链接（官网 / 社区）改放头部导航（见 overrides/partials/header.html），不用 footer social
        "extra": {"generator": False},
        "copyright": "© MarginNote · MarginNote 4 用户手册",
        "nav": _nav(toc),
    }


def write_mkdocs_yml() -> None:
    toc = yaml.safe_load(TOC.read_text(encoding="utf-8")) or []
    MKDOCS_YML.parent.mkdir(parents=True, exist_ok=True)
    MKDOCS_YML.write_text(
        yaml.safe_dump(mkdocs_config(toc), allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
