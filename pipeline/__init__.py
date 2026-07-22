"""MN4 手册构建管线（src/ 规范化，进入 SSG 之前）。

模块：
  assets       —— 共享契约：资源识别 / 分类 / 16 位 path-hash 命名（无重依赖）
  format_page  —— mistletoe 语法树内容转换 → index.md
  format_media —— ffmpeg 媒体编码（webp / gif→mp4 / video→mp4 / copy）

路径布局来自顶层 config.py（pipeline 与 ssg 共用，互不 import）。
本文件承载 doit 任务（task_page / task_media）与发布集加载；dodo.py 仅「导入 + 配置」。
"""

import sys
from pathlib import Path

import yaml

import config
from . import assets, format_page, format_media

SRC = config.SRC
BUILD_SRC = config.BUILD_SRC


def _iter_pages(toc_path):
    data = yaml.safe_load(Path(toc_path).read_text(encoding="utf-8")) or []
    for section in data:
        for cat in (section or {}).get("categories", []) or []:
            for pg in (cat or {}).get("pages", []) or []:
                if isinstance(pg, dict) and pg.get("id"):
                    yield pg


def load_published_ids(toc_path) -> set[str]:
    """读取发布集（section → categories → pages[].id）。"""
    return {str(pg["id"]) for pg in _iter_pages(toc_path)}


def load_slugs(toc_path) -> dict[str, str]:
    """id → slug（英文 URL 目录名）。toc 未配 slug 时回退为 id（保持旧的 id 目录行为）。"""
    return {str(pg["id"]): str(pg.get("slug") or pg["id"]) for pg in _iter_pages(toc_path)}


PUBLISHED = load_published_ids(config.TOC)
SLUGS = load_slugs(config.TOC)              # 输出目录 / 站内链接目标用 slug；媒体哈希仍按源 id


def _slug_relpath(build_rel: str) -> str:
    """build 相对路径 '<id>/image/<hash>.webp' → '<slug>/image/<hash>.webp'（仅换首段目录）。"""
    head, _, tail = build_rel.partition("/")
    return f"{SLUGS.get(head, head)}/{tail}" if tail else build_rel


def task_page():
    """src/<id>/*.md (+toc.yaml) → build/src/<slug>/index.md（中文，默认语言）"""
    for pid in sorted(PUBLISHED):
        md = next((SRC / pid).glob("*.md"), None)
        if md is None:
            continue
        out = BUILD_SRC / SLUGS.get(pid, pid) / "index.md"
        yield {
            "name": pid,
            "file_dep": [str(md), str(config.TOC)],
            "targets": [str(out)],
            "actions": [(format_page.render_page, [str(md), str(out), PUBLISHED, SLUGS])],
            "clean": True,
        }


def _write_en_page(en_md: str, out: str) -> None:
    """i18n/en/<id>.md（译文，链接目标仍是 id）→ build/src/<slug>/index.en.md，改写站内链接目录。"""
    text = format_page.rewrite_internal_links(Path(en_md).read_text(encoding="utf-8"), SLUGS)
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(text.rstrip() + "\n", encoding="utf-8")


def task_page_en():
    """i18n/en/<id>/index.md → build/src/<slug>/index.en.md（英文，mkdocs-static-i18n suffix 结构）。

    仅为已有译文的发布页生成（缺译文则跳过 → 该页仅中文，static-i18n 回退到默认语言）。
    """
    for pid in sorted(PUBLISHED):
        en_md = config.I18N_EN / pid / "index.md"
        if not en_md.exists():
            continue
        out = BUILD_SRC / SLUGS.get(pid, pid) / "index.en.md"
        yield {
            "name": pid,
            "file_dep": [str(en_md), str(config.TOC)],
            "targets": [str(out)],
            "actions": [(_write_en_page, [str(en_md), str(out)])],
            "clean": True,
        }


def _iter_en_media():
    """遍历英文媒体覆盖：yield (覆盖文件, 源相对路径 '<id>/<子目录>/<原名>')。"""
    for sub in assets.ASSET_DIRS:
        for f in sorted(config.I18N_EN.glob(f"*/{sub}/*")):
            if f.is_file():
                yield f, f.relative_to(config.I18N_EN).as_posix()


def task_media_en():
    """i18n/en/<id>/<子目录>/<与中文源同名文件> → build/src/<slug>/…/<hash>.en.<ext>（英文媒体覆盖）。

    哈希仍按中文源路径计算（与正文引用名一致），仅加 .en 语言后缀：static-i18n（suffix）
    令英文站用覆盖版，无覆盖的媒体自动回退中文版。文件名须与中文源完全一致（含扩展名）；
    孤儿覆盖（无同名中文源）不构建，由 media_en_check 报告。
    """
    for f, src_rel in _iter_en_media():
        if not (SRC / src_rel).is_file():
            continue                                   # 孤儿 → media_en_check 警告
        build_rel, kind = assets.out_relpath(src_rel)
        out = BUILD_SRC / assets.en_relpath(_slug_relpath(build_rel))
        yield {
            "name": src_rel,
            "file_dep": [str(f)],
            "targets": [str(out)],
            "actions": [(format_media.encode, [str(f), str(out), kind])],
            "clean": True,
        }


def _report_media_en() -> None:
    """英文媒体覆盖检查（只报告，不构建）：
    ① 孤儿覆盖：i18n/en 下无同名中文源的媒体（不会被构建）；
    ② 缺英文覆盖：已译页面正文引用、而 i18n/en/<id>/<子目录>/ 无同名文件的媒体
       （英文站回退显示中文版）。
    """
    def warn(msg: str) -> None:
        print(f"WARN media_en: {msg}", file=sys.stderr)

    overrides = set()
    for _, src_rel in _iter_en_media():
        overrides.add(src_rel)
        if not (SRC / src_rel).is_file():
            warn(f"孤儿覆盖（无同名中文源，未构建）: i18n/en/{src_rel}")
    missing = 0
    for pid in sorted(PUBLISHED):
        en_md = config.I18N_EN / pid / "index.md"
        if not en_md.exists():
            continue
        ref2src = {}                                   # 页内引用名 <子目录>/<hash>.<ext> → 源相对路径
        for sub in assets.ASSET_DIRS:
            for f in sorted((SRC / pid / sub).glob("*")):
                if f.is_file():
                    ref, _ = format_page.page_ref(f"{sub}/{f.name}", pid)
                    ref2src[ref] = f"{pid}/{sub}/{f.name}"
        for ref in sorted(format_page.collect_local_asset_refs(en_md.read_text(encoding="utf-8"))):
            src_rel = ref2src.get(ref)
            if src_rel is None:
                warn(f"译文引用了无中文源的媒体: {pid}: {ref}")
            elif src_rel not in overrides:
                missing += 1
                warn(f"缺英文覆盖（回退中文）: src/{src_rel}")
    if missing:
        warn(f"共 {missing} 处引用缺英文覆盖（英文站回退显示中文媒体）")


def task_media_en_check():
    """报告英文媒体覆盖状况（孤儿 / 缺覆盖 → stderr 警告；每次构建都运行）。"""
    return {
        "actions": [_report_media_en],
        "uptodate": [False],
    }


def task_media():
    """每个源媒体 → build/src/<slug>/… 内 16 位 path-hash 压缩产物（哈希按源 id 路径，跨语言共用）"""
    for sub in assets.ASSET_DIRS:
        for f in sorted(SRC.glob(f"*/{sub}/*")):
            if not f.is_file():
                continue
            build_rel, kind = assets.out_relpath(f.relative_to(SRC).as_posix())
            out = BUILD_SRC / _slug_relpath(build_rel)
            yield {
                "name": f.relative_to(SRC).as_posix(),
                "file_dep": [str(f)],
                "targets": [str(out)],
                "actions": [(format_media.encode, [str(f), str(out), kind])],
                "clean": True,
            }
