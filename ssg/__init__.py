"""SSG 阶段（mkdocs + Material）：build/src → build/site/。

与规范化管线**解耦、同一 doit 编排**，以 build/src 为交接契约：本包只生成 mkdocs 的
配置、派生页面与静态资源，mkdocs 以子进程调用，构建后再跑 Pagefind 建中文搜索索引。
整包可替换以更换 SSG。所有产物都在 build/ 下（build/mkdocs.yml、build/overrides、build/site）。

模块：
  config —— 从 toc.yaml 生成 build/mkdocs.yml（主题 + 品牌 + 导航 + 搜索接线）
  pages  —— 生成派生页面（首页 hero + 卡片；后续 FAQ / i18n…）
任务（task_config / task_home / task_site / task_search）由仓库根 dodo.py 导入；
逻辑都在包内。
"""

import shutil
import subprocess
import sys
from pathlib import Path

from . import config, pages

_PKG = Path(__file__).parent
STATIC_SRC = _PKG / "static"          # 手维护：stylesheets/ + javascripts/ + mn4-logo.png
OVERRIDES_SRC = _PKG / "overrides"    # 手维护：Material 主题覆盖（Pagefind 头部/搜索框）

DOCS = config.DOCS                    # build/src（mkdocs docs_dir）
SITE = config.SITE                    # build/site
MKDOCS_YML = config.MKDOCS_YML        # build/mkdocs.yml
OVERRIDES = config.OVERRIDES          # build/overrides（custom_dir）


def _run(*args) -> None:
    """以当前（venv）解释器跑模块，避免依赖 PATH 上的 mkdocs / pagefind。"""
    subprocess.run([sys.executable, "-m", *args], check=True)


# ----------------------------------------------------------------------------
# 静态资源：把手维护的 css/js/主题覆盖/logo 拷进 build/
# ----------------------------------------------------------------------------
def _static_pairs() -> list[tuple[Path, Path]]:
    """(源文件, 目标) 列表：static/ → build/src/（含 mn4-logo.png），overrides/ → build/overrides/。"""
    pairs: list[tuple[Path, Path]] = []
    for src_dir, dst_dir in [(STATIC_SRC, DOCS), (OVERRIDES_SRC, OVERRIDES)]:
        for f in sorted(src_dir.rglob("*")):
            if f.is_file():
                pairs.append((f, dst_dir / f.relative_to(src_dir)))
    return pairs


def copy_static() -> None:
    for src, dst in _static_pairs():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def task_config():
    """toc.yaml → build/mkdocs.yml，并把品牌 css/js + 主题覆盖 + logo 拷进 build/。

    两者是同一回事——生成 mkdocs 构建的全部配置输入：配置文件本身，及它引用的
    主题覆盖 / 静态资源。
    """
    pairs = _static_pairs()
    return {
        "file_dep": [str(config.TOC), str(config.TOC_EN)] + [str(s) for s, _ in pairs],
        "targets": [str(MKDOCS_YML)] + [str(d) for _, d in pairs],
        "actions": [config.write_mkdocs_yml, copy_static],
        "clean": True,
    }


def task_home():
    """toc.yaml + 各页 H1/缩略图 → build/src/index.md + index.en.md（中英首页 hero + 卡片）。"""
    page_md = sorted(str(p) for p in DOCS.glob("*/index.md"))
    page_en = sorted(str(p) for p in DOCS.glob("*/index.en.md"))
    return {
        "task_dep": ["page", "page_en"],          # 需中/英正文已规范化（取 H1 / 首图）
        "file_dep": [str(config.TOC), str(config.TOC_EN)] + page_md + page_en,
        "targets": [str(DOCS / "index.md"), str(DOCS / "index.en.md")],
        "actions": [(pages.write_home, [DOCS])],
        "clean": True,
    }


def task_site():
    """mkdocs build → build/site/（依赖 page + media + config + home）。"""
    src_inputs = [str(s) for s, _ in _static_pairs()]
    md_inputs = sorted(str(p) for p in DOCS.rglob("*.md"))
    return {
        "task_dep": ["page", "page_en", "media", "config", "home"],
        "file_dep": [str(MKDOCS_YML)] + md_inputs + src_inputs,
        "targets": [str(SITE / "index.html")],
        "actions": [(_run, ["mkdocs", "build", "-f", str(MKDOCS_YML)])],
        "clean": True,
    }


def _clean_pagefind() -> None:
    shutil.rmtree(SITE / "pagefind", ignore_errors=True)


def task_search():
    """Pagefind 索引（CJK 友好）：在 mkdocs 产出的 build/site 上建 /pagefind/。"""
    return {
        "task_dep": ["site"],
        "file_dep": sorted(str(p) for p in SITE.rglob("*.html")),
        "targets": [str(SITE / "pagefind" / "pagefind.js")],
        "actions": [(_run, ["pagefind", "--site", str(SITE)])],
        "clean": [_clean_pagefind],
    }
