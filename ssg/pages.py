"""生成 SSG 阶段的派生页面（写入 docs_dir = build/src）。

当前：首页 hero + 分区卡片（标题/描述/难度/阅读时长全部取自 toc.yaml；卡片缩略图与
标题从已规范化的各页 build/src/<id>/index.md 读取——遵循“不正则解析 md，遍历语法树”，
用 mistletoe AST 取首个 H1 与首张本地图片）。

后续在此补：FAQ 页（读 src/faq.yaml）、i18n 拼装等。纯 HTML 构造与 IO 分离，便于测试。
"""

from html import escape
from pathlib import Path

import mistletoe
from mistletoe.block_token import Heading
from mistletoe.span_token import Image, RawText
import yaml

HERO_SUB = "从文档阅读、摘录批注，到脑图、卡片与科学复习——MarginNote 4 的完整使用指南。"

DIFFICULTY = {1: "入门 ⭐", 2: "进阶 ⭐⭐", 3: "高级 ⭐⭐⭐"}

FRONT_MATTER = "---\nhide:\n  - navigation\n  - toc\n---\n"


# ----------------------------------------------------------------------------
# 读取已规范化页面的元数据（AST，不用正则解析 md）
# ----------------------------------------------------------------------------
def _walk(token):
    yield token
    for child in getattr(token, "children", None) or []:
        yield from _walk(child)


def _inline_text(token) -> str:
    return "".join(t.content for t in _walk(token) if isinstance(t, RawText)).strip()


def read_page_meta(page_dir: Path) -> tuple[str | None, str | None]:
    """返回 (H1 标题, 首张本地图片相对路径 image/xxx)，缺失则为 None。"""
    md = Path(page_dir) / "index.md"
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
def difficulty_label(level) -> str:
    return DIFFICULTY.get(level, "")


def card_html(page_id: str, title: str, desc, difficulty, read_time, thumb) -> str:
    href = f"{page_id}/"
    thumb_block = ""
    if thumb:
        src = escape(href + thumb)
        thumb_block = (f'<div class="mn-card__thumb">'
                       f'<img src="{src}" alt="" loading="lazy" class="off-glb"></div>')
    meta = []
    if difficulty_label(difficulty):
        meta.append(f'<span class="mn-card__diff">{escape(difficulty_label(difficulty))}</span>')
    if read_time:
        meta.append(f'<span class="mn-card__time">🕐 {int(read_time)} 分钟</span>')
    meta_block = f'<div class="mn-card__meta">{"".join(meta)}</div>' if meta else ""
    desc_block = f'<p class="mn-card__desc">{escape(str(desc))}</p>' if desc else ""
    return (
        f'<a class="mn-card" href="{escape(href)}">{thumb_block}'
        f'<div class="mn-card__body">'
        f'<h4 class="mn-card__title">{escape(title)}</h4>'
        f'{desc_block}{meta_block}</div></a>'
    )


def category_html(cat: dict, cards: list[str]) -> str:
    if not cards:
        return ""
    head = (
        '<div class="mn-cat__head">'
        f'<span class="mn-cat__icon">{escape(str(cat.get("icon", "")))}</span>'
        f'<h3 class="mn-cat__name">{escape(str(cat.get("category", "")))}</h3>'
        f'<span class="mn-cat__desc">{escape(str(cat.get("desc", "")))}</span>'
        '</div>'
    )
    return (f'<div class="mn-cat">{head}'
            f'<div class="mn-cards">{"".join(cards)}</div></div>')


def section_html(section: dict, categories: list[str]) -> str:
    cats = [c for c in categories if c]
    if not cats:
        return ""
    title = section.get("section") or section.get("title") or ""
    head = (
        '<header class="mn-section__head">'
        f'<span class="mn-section__label">{escape(str(section.get("label", "")))}</span>'
        f'<h2>{escape(str(title))}</h2>'
        f'<p class="mn-section__desc">{escape(str(section.get("desc", "")))}</p>'
        '</header>'
    )
    return f'<section class="mn-section">{head}{"".join(cats)}</section>'


def hero_html() -> str:
    return (
        '<section class="mn-hero">'
        '<img class="mn-hero__logo" src="mn4-logo.png" alt="MarginNote 4"'
        ' width="76" height="76">'
        '<h1 class="mn-hero__title">MarginNote 4 用户手册</h1>'
        f'<p class="mn-hero__sub">{escape(HERO_SUB)}</p>'
        '</section>'
    )


# ----------------------------------------------------------------------------
# 组装（IO：读各页 AST 取标题/缩略图）
# ----------------------------------------------------------------------------
def build_home(toc, src_dir: Path) -> str:
    src_dir = Path(src_dir)
    # 全站正文为全宽；首页用 .mn-home 收窄居中（见 extra.css）。
    blocks = [FRONT_MATTER, '<div class="mn-home">', hero_html()]
    for section in toc or []:
        cat_blocks = []
        for cat in (section or {}).get("categories", []) or []:
            cards = []
            for pg in (cat or {}).get("pages", []) or []:
                pid = pg.get("id")
                if not pid:
                    continue
                title, thumb = read_page_meta(src_dir / pid)
                cards.append(card_html(
                    pid,
                    title or str(pg.get("id")),
                    pg.get("desc"),
                    pg.get("difficulty"),
                    pg.get("read_time"),
                    thumb,
                ))
            cat_blocks.append(category_html(cat, cards))
        blocks.append(section_html(section, cat_blocks))
    blocks.append("</div>")
    return "\n".join(b for b in blocks if b) + "\n"


def write_home(toc_path, src_dir) -> None:
    toc = yaml.safe_load(Path(toc_path).read_text(encoding="utf-8")) or []
    out = Path(src_dir) / "index.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_home(toc, src_dir), encoding="utf-8")
