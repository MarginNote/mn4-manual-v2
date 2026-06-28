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


def load_published_ids(toc_path) -> set[str]:
    """读取发布集（section → categories → pages[].id）。"""
    data = yaml.safe_load(Path(toc_path).read_text(encoding="utf-8")) or []
    ids: set[str] = set()
    for section in data:
        for cat in (section or {}).get("categories", []) or []:
            for pg in (cat or {}).get("pages", []) or []:
                if isinstance(pg, dict) and pg.get("id"):
                    ids.add(str(pg["id"]))
    return ids


PUBLISHED = load_published_ids(config.TOC)


def task_page():
    """src/<id>/*.md (+toc.yaml) → build/src/<id>/index.md"""
    for pid in sorted(PUBLISHED):
        md = next((SRC / pid).glob("*.md"), None)
        if md is None:
            continue
        out = BUILD_SRC / pid / "index.md"
        yield {
            "name": pid,
            "file_dep": [str(md), str(config.TOC)],
            "targets": [str(out)],
            "actions": [(format_page.render_page, [str(md), str(out), PUBLISHED])],
            "clean": True,
        }


def task_media():
    """每个源媒体 → build 内 16 位 path-hash 压缩产物"""
    for sub in assets.ASSET_DIRS:
        for f in sorted(SRC.glob(f"*/{sub}/*")):
            if not f.is_file():
                continue
            build_rel, kind = assets.out_relpath(f.relative_to(SRC).as_posix())
            out = BUILD_SRC / build_rel
            yield {
                "name": f.relative_to(SRC).as_posix(),
                "file_dep": [str(f)],
                "targets": [str(out)],
                "actions": [(format_media.encode, [str(f), str(out), kind])],
                "clean": True,
            }
