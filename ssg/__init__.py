"""SSG 阶段（mkdocs + Material）：build/src → build/site/。

与规范化管线**解耦、同一 doit 编排**，以 build/src 为交接契约：本包只生成 mkdocs 的
配置与派生页面，mkdocs 以子进程调用。整包可替换以更换 SSG。
所有产物都在 build/ 下（build/mkdocs.yml、build/site）。

模块：
  config —— 从 toc.yaml 生成 build/mkdocs.yml（主题 + 导航）
  pages  —— 生成派生页面（首页占位；后续 FAQ / i18n…）
任务（task_config / task_site）由仓库根 dodo.py 导入；逻辑都在包内。
"""

import subprocess
import sys

from . import config, pages

DOCS = config.DOCS               # build/src（mkdocs docs_dir）
SITE = config.SITE               # build/site
MKDOCS_YML = config.MKDOCS_YML   # build/mkdocs.yml


def _run(*args) -> None:
    """以当前（venv）解释器跑模块，避免依赖 PATH 上的 mkdocs。"""
    subprocess.run([sys.executable, "-m", *args], check=True)


def task_config():
    """toc.yaml → build/mkdocs.yml；并生成首页占位 build/src/index.md"""
    return {
        "file_dep": [str(config.TOC)],
        "targets": [str(MKDOCS_YML), str(DOCS / "index.md")],
        "actions": [config.write_mkdocs_yml, (pages.write_home, [DOCS / "index.md"])],
        "clean": True,
    }


def task_site():
    """mkdocs build → build/site/（依赖 page + media + config）"""
    return {
        "task_dep": ["page", "media", "config"],
        "file_dep": [str(MKDOCS_YML)] + sorted(str(p) for p in DOCS.rglob("*.md")),
        "targets": [str(SITE / "index.html")],
        "actions": [(_run, ["mkdocs", "build", "-f", str(MKDOCS_YML)])],
        "clean": True,
    }
