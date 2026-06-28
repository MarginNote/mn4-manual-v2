"""生成 SSG 阶段的派生页面（写入 docs_dir = build/src）。

当前仅首页占位；后续在此补：hero 首页、FAQ 页（读 src/faq.yaml）、难度·阅读时长卡片等。
"""

from pathlib import Path

HOME = (
    "# MarginNote 4 用户手册\n\n"
    "> 首页占位 —— 后续补 hero / 难度·阅读时长卡片 / FAQ（读 `src/faq.yaml`）。\n"
)


def write_home(out) -> None:
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(HOME, encoding="utf-8")
