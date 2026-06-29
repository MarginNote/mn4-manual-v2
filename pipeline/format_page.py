"""format_page.py —— Markdown 内容转换（遍历 mistletoe 语法树，绝不正则解析 MD）。

每页应用：
  1. 章节规范化：保留首个标题为 h1；正文标题按祖先栈重排为**连续不跳级**的层级
     （从 h2 起）——既把 wolai 的多个 `#` 章节降为 h2，也把缺上级的 `###` 升级。
  2. 跨页链接（纯 id）：`wolai.com/<id>` 与根相对 `/<id>`；发布集内 → `../<id>/index.md`
     （去深锚）；自链接 / 悬空 → 降级为纯文本；外链原样。
  3. 媒体引用：改写为 build 内 16 位 path-hash 名（见 assets）；gif/视频统一为动画 webp（仍是 <img>）；
     引用但磁盘缺失 → 降级（图片去掉、保留 alt 文本）并记录。
  4. 表格单元格：wolai 把单元格内图片/链接 markdown 反斜杠转义而被当作字面文本；
     检测到转义序列即按去转义后字面量重新分词（见 walk_table，仍走 mistletoe）。

注：正则只作用于 URL 字符串（id 提取），不解析 Markdown。
本模块只转换**单页**（render_page）；发布集由调用方（dodo）传入，与 toc 解耦。
"""

from __future__ import annotations

import re
from pathlib import Path

import mistletoe
from mistletoe import block_token as B, span_token as S
from mistletoe.markdown_renderer import MarkdownRenderer

from . import assets

WOLAI_HOST_RE = re.compile(r"^https?://(?:www\.)?wolai\.com/(.+)$", re.I)
WOLAI_ID_RE = re.compile(r"[0-9A-Za-z]{20,24}")      # wolai 页面 id（实测 21~22 位）
ROOT_ID_RE = re.compile(r"^/([0-9A-Za-z]{20,24})(?:[#/?].*)?$")
HTTP_RE = re.compile(r"^https?://", re.I)
# 已规范化正文里的站内链接（`../<id>/index.md`）——用于把 id 目录改写成 slug 目录。
INTERNAL_LINK_RE = re.compile(r"\.\./([0-9A-Za-z]{20,24})/index\.md")


def rewrite_internal_links(text: str, id2slug: dict) -> str:
    """把已规范化文本里的 `../<id>/index.md` 改写为 `../<slug>/index.md`。

    供 EN 译文（i18n/en/<id>.md，链接目标仍是 id）落盘到 slug 目录前做目录改写；
    媒体引用是页内相对路径（image/…），不受目录改名影响，无需改写。
    """
    if not id2slug:
        return text
    return INTERNAL_LINK_RE.sub(
        lambda m: f"../{id2slug.get(m.group(1), m.group(1))}/index.md", text)


# ---------------------------------------------------------------------------
# URL 工具
# ---------------------------------------------------------------------------

def extract_page_id(url: str) -> str | None:
    """从 wolai.com/<id> 或根相对 /<id> 提取页面 id；否则 None（作用于 URL 字符串）。"""
    m = WOLAI_HOST_RE.match(url)
    if m:
        first = re.split(r"[#?]", m.group(1), maxsplit=1)[0]
        for seg in reversed(first.split("/")):
            if WOLAI_ID_RE.fullmatch(seg):
                return seg
        return None
    m = ROOT_ID_RE.match(url)
    return m.group(1) if m else None


def page_ref(rel: str, pid: str) -> tuple[str, str]:
    """页内资源相对引用 'image/foo.png' → (改写后页内引用 'image/<hash>.webp', kind)。"""
    build_rel, kind = assets.out_relpath(f"{pid}/{rel}")
    return f"{Path(rel).parent.as_posix()}/{Path(build_rel).name}", kind


# ---------------------------------------------------------------------------
# AST 节点构造 / 文本
# ---------------------------------------------------------------------------

def _tokenize_inline(text: str) -> list:
    """把（去转义后的）字面文本重新分词为**内联**节点。

    用 mistletoe 的行内分词器（不是 Document：那会做块级解析，可能把 ListItem 等块节点
    塞进表格单元格而无法按内联渲染）。仍是遍历语法树，不正则解析 MD。
    """
    return list(S.tokenize_inner(text)) if text else []


def inline_text(children) -> str:
    parts = []
    for t in children or []:
        if isinstance(t, S.RawText):
            parts.append(t.content)
        elif isinstance(t, S.LineBreak):
            parts.append(" ")
        elif getattr(t, "children", None):
            parts.append(inline_text(t.children))
    return "".join(parts)


# ---------------------------------------------------------------------------
# 转换
# ---------------------------------------------------------------------------

def normalize_headings(doc, stat: dict) -> None:
    """章节规范化：首个标题→h1；正文标题按祖先栈重排为连续层级（从 h2 起）。"""
    heads: list = []

    def collect(tok):
        for c in getattr(tok, "children", []) or []:
            if isinstance(c, (B.Heading, B.SetextHeading)):
                heads.append(c)
            collect(c)

    collect(doc)
    if not heads:
        return
    origs = [h.level for h in heads]
    if heads[0].level != 1:
        heads[0].level = 1
        stat["normalized"] += 1
    stack: list[int] = []
    for h, lvl in zip(heads[1:], origs[1:]):
        while stack and stack[-1] >= lvl:
            stack.pop()
        stack.append(lvl)
        new_level = len(stack) + 1                # 顶层正文章节 = h2
        if h.level != new_level:
            h.level = new_level
            stat["normalized"] += 1


def handle_link(tok, ctx: dict) -> list:
    tok.children = process_inline(tok.children, ctx)     # 先处理嵌套
    target = tok.target or ""
    if assets.is_local_asset(target):
        if not (ctx["page_dir"] / target).exists():
            ctx["stat"]["missing"] += 1
            ctx["missing"].append((ctx["id"], target))
            return list(tok.children)
        ref, _ = page_ref(target, ctx["id"])
        tok.target, tok.title, tok.dest_type = ref, "", "uri"
        return [tok]
    pid = extract_page_id(target)
    if pid:
        if pid == ctx["id"]:
            ctx["stat"]["self"] += 1
            return list(tok.children)
        if pid in ctx["published"]:
            ctx["stat"]["internal"] += 1
            slug = ctx["id2slug"].get(pid, pid)       # slug 目录（未配置 slug 时回退为 id）
            tok.target, tok.title, tok.dest_type = f"../{slug}/index.md", "", "uri"
            return [tok]
        ctx["stat"]["dangling"] += 1
        return list(tok.children)
    ctx["stat"]["external"] += 1
    return [tok]


def handle_image(tok, ctx: dict) -> list:
    src = tok.src or ""
    if assets.is_local_asset(src):
        if not (ctx["page_dir"] / src).exists():
            ctx["stat"]["missing"] += 1
            ctx["missing"].append((ctx["id"], src))
            return list(tok.children)                    # 降级为 alt 文本
        ref, kind = page_ref(src, ctx["id"])             # gif/视频已统一为动画 webp → 仍是 <img>
        if kind == "webp_anim":
            ctx["stat"]["anim"] += 1
        tok.src, tok.title, tok.dest_type = ref, "", "uri"
        return [tok]
    if HTTP_RE.match(src):
        ctx["stat"]["external"] += 1
        return [tok]
    ctx["stat"]["missing"] += 1                           # 坏图占位
    ctx["missing"].append((ctx["id"], src))
    return list(tok.children)


def process_inline(children, ctx: dict) -> list:
    out: list = []
    for tok in children or []:
        if isinstance(tok, S.Image):
            out.extend(handle_image(tok, ctx))
        elif isinstance(tok, S.Link):
            out.extend(handle_link(tok, ctx))
        elif isinstance(tok, (S.Emphasis, S.Strong, S.Strikethrough)):
            tok.children = process_inline(tok.children, ctx)
            out.append(tok)
        else:
            out.append(tok)
    return out


def walk_table(tbl, ctx: dict) -> None:
    rows = ([tbl.header] if getattr(tbl, "header", None) is not None else []) + list(tbl.children or [])
    for row in rows:
        for cell in row.children or []:
            kids = cell.children or []
            # wolai 在表格单元格里把图片/链接的 markdown 反斜杠转义（\[ \( \< …），令其被解析
            # 为字面文本而非 Image/Link。检测到转义序列时，按去转义后的字面量重新分词（仍走
            # mistletoe，不正则解析），让图片/链接复原为节点再处理。
            if any(isinstance(t, S.EscapeSequence) for t in kids):
                kids = _tokenize_inline(inline_text(kids))
            cell.children = process_inline(kids, ctx)


def walk_blocks(tok, ctx: dict) -> None:
    """遍历块级语法树；叶块处理内联，容器块递归。代码块自然不被触及。"""
    for child in getattr(tok, "children", []) or []:
        if isinstance(child, (B.Paragraph, B.Heading, B.SetextHeading)):
            child.children = process_inline(child.children, ctx)
        elif isinstance(child, B.Table):
            walk_table(child, ctx)
        elif isinstance(child, B.TableCell):
            child.children = process_inline(child.children, ctx)
        else:
            walk_blocks(child, ctx)


def _new_stat() -> dict:
    return {"normalized": 0, "internal": 0, "self": 0, "dangling": 0,
            "external": 0, "missing": 0, "anim": 0}


def render_page(md_path, out_path, published, id2slug=None) -> dict:
    """转换单页 → 写 build/src/<slug>/index.md。返回统计（含 missing_list）。

    id2slug：站内链接目标 id → slug 目录名（缺省/未配置 → 回退为 id，保持旧行为）。
    媒体哈希仍按**源** id 路径计算（见 assets），与 slug 解耦。
    """
    md_path, out_path = Path(md_path), Path(out_path)
    pid = md_path.parent.name
    stat = _new_stat()
    missing: list = []
    ctx = {"id": pid, "page_dir": md_path.parent, "published": published,
           "stat": stat, "missing": missing, "id2slug": id2slug or {}}
    with MarkdownRenderer() as renderer:
        doc = mistletoe.Document(md_path.read_text(encoding="utf-8"))
        normalize_headings(doc, stat)
        walk_blocks(doc, ctx)
        body = renderer.render(doc)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(body.rstrip() + "\n", encoding="utf-8")
    stat["missing_list"] = missing
    return stat
