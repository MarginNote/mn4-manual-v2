"""MN4 手册构建管线（src/ 规范化，进入 SSG 之前）。

模块：
  assets       —— 共享契约：资源识别 / 分类 / 16 位 path-hash 命名（无重依赖）
  format_page  —— mistletoe 语法树内容转换 → index.md
  format_media —— ffmpeg 媒体编码（webp / gif→mp4 / video→mp4 / copy）

路径布局来自顶层 config.py（pipeline 与 ssg 共用，互不 import）。
本文件承载 doit 任务（task_page / task_media）与发布集加载；dodo.py 仅「导入 + 配置」。
"""

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
