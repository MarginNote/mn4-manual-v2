"""生成 SSG 阶段的派生页面（写入 docs_dir = build/src）。

首页 hero + 分区卡片，中英双语：index.md（中文，默认语言）+ index.en.md（英文，/en/）。
标题/描述/难度/阅读时长取自 toc.yaml（英文取 *_en 字段，缺则回退中文）；卡片缩略图与标题
从各页 build/src/<slug>/index{,.en}.md 读取——遵循“不正则解析 md，遍历语法树”，用 mistletoe
AST 取首个 H1 与首张本地图片。卡片链接用 slug 目录（英文页相对链接自然落到 /en/<slug>/）。

纯 HTML 构造与 IO 分离，便于测试。
"""

from html import escape
from pathlib import Path

import mistletoe
from mistletoe.block_token import Heading
from mistletoe.span_token import Image, RawText

from . import config

# 每语言的界面文案（首页 hero / 难度标签 / 阅读时长单位 / 文件名）。
LANG = {
    "zh": {
        "site_title": "MarginNote 4 用户手册",
        "hero_sub": "从文档阅读、摘录批注，到脑图、卡片与科学复习——MarginNote 4 的完整使用指南。",
        "difficulty": {1: "入门 ⭐", 2: "进阶 ⭐⭐", 3: "高级 ⭐⭐⭐"},
        "minutes": "🕐 {n} 分钟",
        "index": "index.md",
    },
    "en": {
        "site_title": "MarginNote 4 User Manual",
        "hero_sub": "From reading documents and making excerpts to mind maps, cards, and "
                    "spaced repetition — the complete guide to MarginNote 4.",
        "difficulty": {1: "Beginner ⭐", 2: "Intermediate ⭐⭐", 3: "Advanced ⭐⭐⭐"},
        "minutes": "🕐 {n} min",
        "index": "index.en.md",
    },
}

FRONT_MATTER = "---\nhide:\n  - navigation\n  - toc\n---\n"


def _media_prefix(lang: str) -> str:
    """首页到站点根的相对前缀：中文首页在 /（空），英文首页在 /en/（需 ../）。

    首页是生成的 HTML，static-i18n 不会改写其跨目录引用；媒体单份存于默认语言根下，
    故英文首页引用 logo / 卡片缩略图时要回退一级。正文页的图片由 static-i18n 自行改写。
    """
    return "../" if lang == "en" else ""


# ----------------------------------------------------------------------------
# 取 toc 字段：英文取 <key>_en，缺则回退中文 <key>
# ----------------------------------------------------------------------------
def _f(obj: dict, key: str, lang: str):
    if lang == "en":
        v = obj.get(f"{key}_en")
        if v:
            return v
    return obj.get(key)


# ----------------------------------------------------------------------------
# 读取已规范化页面的元数据（AST，不用正则解析 md）
# ----------------------------------------------------------------------------
def _walk(token):
    yield token
    for child in getattr(token, "children", None) or []:
        yield from _walk(child)


def _inline_text(token) -> str:
    return "".join(t.content for t in _walk(token) if isinstance(t, RawText)).strip()


def read_page_meta(page_dir: Path, filename: str = "index.md") -> tuple[str | None, str | None]:
    """返回 (H1 标题, 首张本地图片相对路径 image/xxx)，缺失则为 None。"""
    md = Path(page_dir) / filename
    if not md.exists():
        return (None, None)
    with md.open(encoding="utf-8") as f:
        doc = mistletoe.Document(f)
    title: str | None = None
    thumb: str | None = None
    for tok in _walk(doc):
        if title is None and isinstance(tok, Heading) and tok.level == 1:
            title = _inline_text(tok)
        if thumb is None and isinstance(tok, Image) and (tok.src or "").startswith("image/"):
            thumb = tok.src
        if title is not None and thumb is not None:
            break
    return (title, thumb)


# ----------------------------------------------------------------------------
# 纯 HTML 构造（无 IO，便于单元测试）
# ----------------------------------------------------------------------------
def card_html(slug: str, title: str, desc, difficulty, read_time, thumb, lang: str) -> str:
    href = f"{slug}/"                       # 链接：同语言相对（中文→/slug/，英文→/en/slug/）
    thumb_block = ""
    if thumb:
        src = escape(_media_prefix(lang) + href + thumb)   # 缩略图：跨目录指向根下单份媒体
        thumb_block = (f'<div class="mn-card__thumb">'
                       f'<img src="{src}" alt="" loading="lazy" class="off-glb"></div>')
    meta = []
    diff_label = LANG[lang]["difficulty"].get(difficulty, "")
    if diff_label:
        meta.append(f'<span class="mn-card__diff">{escape(diff_label)}</span>')
    if read_time:
        meta.append(f'<span class="mn-card__time">{escape(LANG[lang]["minutes"].format(n=int(read_time)))}</span>')
    meta_block = f'<div class="mn-card__meta">{"".join(meta)}</div>' if meta else ""
    desc_block = f'<p class="mn-card__desc">{escape(str(desc))}</p>' if desc else ""
    return (
        f'<a class="mn-card" href="{escape(href)}">{thumb_block}'
        f'<div class="mn-card__body">'
        f'<h4 class="mn-card__title">{escape(title)}</h4>'
        f'{desc_block}{meta_block}</div></a>'
    )


def category_html(cat: dict, cards: list[str], lang: str) -> str:
    if not cards:
        return ""
    head = (
        '<div class="mn-cat__head">'
        f'<span class="mn-cat__icon">{escape(str(cat.get("icon", "")))}</span>'
        f'<h3 class="mn-cat__name">{escape(str(_f(cat, "category", lang) or ""))}</h3>'
        f'<span class="mn-cat__desc">{escape(str(_f(cat, "desc", lang) or ""))}</span>'
        '</div>'
    )
    return (f'<div class="mn-cat">{head}'
            f'<div class="mn-cards">{"".join(cards)}</div></div>')


def section_html(section: dict, categories: list[str], lang: str) -> str:
    cats = [c for c in categories if c]
    if not cats:
        return ""
    title = _f(section, "title", lang) or section.get("section") or ""
    head = (
        '<header class="mn-section__head">'
        f'<span class="mn-section__label">{escape(str(section.get("label", "")))}</span>'
        f'<h2>{escape(str(title))}</h2>'
        f'<p class="mn-section__desc">{escape(str(_f(section, "desc", lang) or ""))}</p>'
        '</header>'
    )
    return f'<section class="mn-section">{head}{"".join(cats)}</section>'


def hero_html(lang: str) -> str:
    s = LANG[lang]
    return (
        '<section class="mn-hero">'
        f'<img class="mn-hero__logo" src="{_media_prefix(lang)}mn4-logo.png" alt="{escape(s["site_title"])}"'
        ' width="76" height="76">'
        f'<h1 class="mn-hero__title">{escape(s["site_title"])}</h1>'
        f'<p class="mn-hero__sub">{escape(s["hero_sub"])}</p>'
        '</section>'
    )


# ----------------------------------------------------------------------------
# 组装（IO：读各页 AST 取标题/缩略图）
# ----------------------------------------------------------------------------
def build_home(toc, src_dir: Path, lang: str = "zh") -> str:
    src_dir = Path(src_dir)
    fname = LANG[lang]["index"]
    # 全站正文为全宽；首页用 .mn-home 收窄居中（见 extra.css）。
    blocks = [FRONT_MATTER, '<div class="mn-home">', hero_html(lang)]
    for section in toc or []:
        cat_blocks = []
        for cat in (section or {}).get("categories", []) or []:
            cards = []
            for pg in (cat or {}).get("pages", []) or []:
                pid = pg.get("id")
                if not pid:
                    continue
                slug = str(pg.get("slug") or pid)
                # 英文卡片标题取 EN 页 H1，缺则回退中文页 H1，再回退 slug。
                title, thumb = read_page_meta(src_dir / slug, fname)
                if title is None and lang == "en":
                    title, thumb = read_page_meta(src_dir / slug, "index.md")
                cards.append(card_html(
                    slug,
                    title or slug,
                    _f(pg, "desc", lang),
                    pg.get("difficulty"),
                    pg.get("read_time"),
                    thumb,
                    lang,
                ))
            cat_blocks.append(category_html(cat, cards, lang))
        blocks.append(section_html(section, cat_blocks, lang))
    blocks.append("</div>")
    return "\n".join(b for b in blocks if b) + "\n"


def write_home(src_dir) -> None:
    """生成中英双语首页：index.md（中文）+ index.en.md（英文，mkdocs-static-i18n suffix）。

    目录数据用 config.load_merged_toc()（中文 + slug ⊕ 英文 overlay），英文卡片描述取 *_en。
    """
    toc = config.load_merged_toc()
    src_dir = Path(src_dir)
    src_dir.mkdir(parents=True, exist_ok=True)
    for lang in ("zh", "en"):
        (src_dir / LANG[lang]["index"]).write_text(build_home(toc, src_dir, lang), encoding="utf-8")
