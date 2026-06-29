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

import datetime
import re

import yaml

from config import (  # noqa: F401  (部分名字供 ssg 包其它模块复用)
    BUILD_SRC,
    MKDOCS_YML,
    OVERRIDES,
    SITE,
    SITE_DESCRIPTION,
    SITE_URL,
    TOC,
    TOC_EN,
)

DOCS = BUILD_SRC                 # mkdocs docs_dir = build/src
_YEAR = datetime.date.today().year   # 版权年份（构建时）；ICP / 社交链接见 overrides/partials/copyright.html


def load_merged_toc() -> list:
    """src/toc.yaml（中文 + slug）⊕ i18n/en/toc.yaml（英文 overlay）→ 内存合并的目录结构。

    只在内存里把 *_en 贴到对应节点上（sections/categories 按中文名匹配，pages 按 id）；
    两个源文件都不被改写。slug 本就在 toc.yaml（语言无关的页面标识），故 pipeline 直接读
    toc.yaml 即可，无需 overlay；只有 ssg（导航英译 / 英文首页）需要这份合并结果。
    """
    toc = yaml.safe_load(TOC.read_text(encoding="utf-8")) or []
    ov = (yaml.safe_load(TOC_EN.read_text(encoding="utf-8")) if TOC_EN.exists() else {}) or {}
    sec_en, cat_en, pg_en = ov.get("sections", {}), ov.get("categories", {}), ov.get("pages", {})
    for s in toc:
        s.update({k: v for k, v in (sec_en.get(s.get("section")) or {}).items() if v})
        for c in s.get("categories", []) or []:
            c.update({k: v for k, v in (cat_en.get(c.get("category")) or {}).items() if v})
            for p in c.get("pages", []) or []:
                p.update({k: v for k, v in (pg_en.get(p.get("id")) or {}).items() if v})
    return toc


def _slug(pg) -> str:
    return str(pg.get("slug") or pg.get("id"))


def _nav(toc) -> list:
    """toc.yaml（section → category → pages）→ mkdocs nav（含首页）。页面路径用 slug 目录。"""
    nav: list = [{"首页": "index.md"}]
    for section in toc or []:
        cats = []
        for cat in (section or {}).get("categories", []) or []:
            pages = [f"{_slug(pg)}/index.md"
                     for pg in (cat or {}).get("pages", []) or [] if pg.get("id")]
            if pages:
                cats.append({cat.get("category", "?"): pages})
        if cats:
            nav.append({section.get("section") or section.get("title") or "?": cats})
    return nav


def _nav_translations(toc) -> dict:
    """默认语言（中文）导航标题 → 英文（mkdocs-static-i18n 按标题字符串匹配）。

    页面标题由各 EN 页 H1 自动派生，无需在此映射；这里只译分区名与分类名 + 首页。
    分区名形如 "📄 文档"：保留首个中文字符前的 emoji 前缀，其后整体替换为 title_en
    （不靠 title 子串匹配——section 名与 title 的中文用词/语序可能不同）。
    缺英文（未译）则不加该条 → 该导航项回退显示中文。
    """
    out = {"首页": "Home"}
    for section in toc or []:
        sec_name = section.get("section") or ""
        title_en = section.get("title_en")
        if sec_name and title_en:
            m = re.search(r"[一-鿿]", sec_name)      # 首个中文字符 → 之前的是 emoji 前缀
            out[sec_name] = (sec_name[:m.start()] if m else "") + title_en
        for cat in (section or {}).get("categories", []) or []:
            name, name_en = cat.get("category"), cat.get("category_en")
            if name and name_en:
                out[name] = name_en
    return out


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
        # i18n：中文为默认语言（根 URL 不变），英文走 /en/ 子路径（suffix 结构：index.en.md）。
        # 媒体在默认语言目录内单份存放，static-i18n 自动把 /en/ 页面的相对引用回指，无副本。
        "plugins": [
            {"i18n": {
                "docs_structure": "suffix",
                "fallback_to_default": True,        # 缺英文译文的页 → 回退显示中文
                "reconfigure_material": True,       # 按语言切换 Material 界面文案 / lang
                "reconfigure_search": False,        # 搜索用 Pagefind，非 Material 内置
                "languages": [
                    {"locale": "zh", "default": True, "name": "中文", "build": True},
                    {"locale": "en", "name": "English", "build": True,
                     "site_name": "MarginNote 4 User Manual",
                     # 英文站名 / 描述 / 版权：static-i18n 按语言覆盖（免去自定义 partial）
                     "site_description": (
                         "The complete MarginNote 4 user manual — your guide to deep learning "
                         "with PDFs, notes, and mind maps. Covers document notes, mind maps, "
                         "card review, AI features, and advanced tips."),
                     "copyright": f"© {_YEAR} MarginNote · MarginNote 4 User Manual",
                     # 英文页脚社交（覆盖默认中文社交）：static-i18n 合并 extra，保留 generator/alternate
                     "extra": {"social": [
                         {"icon": "fontawesome/brands/x-twitter",
                          "link": "https://twitter.com/marginnoteapp", "name": "X / Twitter"}]},
                     "nav_translations": _nav_translations(toc)},
                ],
            }},
            "glightbox",
        ],
        "markdown_extensions": [
            "tables", "attr_list", "md_in_html", "admonition", "footnotes",
            "pymdownx.superfences", "pymdownx.details",
            {"toc": {"permalink": True}},
        ],
        # 相对路径（无前导 /）：Material 的 `| url` 按页面深度改写，故在任意子路径前缀下都正确。
        # Pagefind 资源在站点根 /pagefind/（构建后生成）；pagefind-ui.js 自动按自身 URL 定位 bundle。
        "extra_css": ["stylesheets/extra.css", "pagefind/pagefind-ui.css"],
        "extra_javascript": ["pagefind/pagefind-ui.js", "javascripts/pagefind-init.js"],
        # 跨站链接（官网/社区）在头部（见 header.html）。页脚社交用 Material 原生 extra.social
        # （图标在页脚右下、与版权同行）；这是中文默认列表，英文见上方语言覆盖。
        "extra": {
            "generator": False,
            "social": [
                {"icon": "simple/xiaohongshu", "name": "小红书",
                 "link": "https://www.xiaohongshu.com/user/profile/62de06bd000000001f017b4d"},
                {"icon": "simple/bilibili", "name": "Bilibili",
                 "link": "https://space.bilibili.com/183940526"},
                {"icon": "fontawesome/brands/weixin", "name": "微信公众号",
                 "link": "https://mp.weixin.qq.com/s/RGyzJD078p27QRqs5NHBag"},
            ],
        },
        # 中文版权附 ICP 备案（config.copyright 支持 HTML，Material 原样渲染）；英文版权见语言覆盖（无 ICP）。
        "copyright": (f'© {_YEAR} MarginNote · MarginNote 4 用户手册 · '
                      '<a href="http://www.beian.miit.gov.cn/" target="_blank" rel="noopener">京ICP备2021022247号-2</a>'),
        "nav": _nav(toc),
    }


def write_mkdocs_yml() -> None:
    toc = load_merged_toc()                 # 中文 + slug ⊕ 英文 overlay（导航英译用）
    MKDOCS_YML.parent.mkdir(parents=True, exist_ok=True)
    MKDOCS_YML.write_text(
        yaml.safe_dump(mkdocs_config(toc), allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
