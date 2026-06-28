"""assets.py —— 构建管线的命名 / 分类契约。

唯一真相来源：哪些 URL 是页内本地资源、每个资源压缩成什么格式、产物叫什么名字。
纯字符串/哈希逻辑，不依赖目录布局（见顶层 config.py）、不依赖 mistletoe / ffmpeg，便于单测。
format_page、format_media、dodo 都调用本模块，保证「正文引用名 / 磁盘文件名 / doit 构建
目标」三者一致。

命名：build 内资源名 = md5(源相对路径)[:16] + 新后缀（path-hash，非内容哈希）。
  - 由「路径」决定（非字节）→ 确定、增量安全、不耦合正文与媒体内容。
  - 纯 ASCII → 免 URL 编码；定长 → 无冲突；同时抹掉原始文件名里的拍摄元数据。
"""

from __future__ import annotations

import hashlib
from pathlib import Path

ASSET_DIRS = ("image", "video", "file")          # 页内资源子目录
IMG_EXT = {".png", ".jpg", ".jpeg"}              # → webp
GIF_EXT = {".gif"}                               # → mp4（动画）
VID_EXT = {".mp4", ".mov", ".webm", ".m4v"}      # → mp4（重编码）

HASH_LEN = 16


def is_local_asset(url: str) -> bool:
    """markdown URL 是否指向页内本地资源（image/ video/ file/）。"""
    return bool(url) and "://" not in url and url.split("/", 1)[0] in ASSET_DIRS


def classify(ext: str) -> str:
    """源扩展名 → 编码 kind（webp | mp4_gif | mp4_video | copy）。"""
    e = ext.lower()
    if e in IMG_EXT:
        return "webp"
    if e in GIF_EXT:
        return "mp4_gif"
    if e in VID_EXT:
        return "mp4_video"
    return "copy"


def _out_ext(kind: str, src_suffix: str) -> str:
    if kind == "webp":
        return ".webp"
    if kind in ("mp4_gif", "mp4_video"):
        return ".mp4"
    return src_suffix.lower()


def out_relpath(src_rel: str) -> tuple[str, str]:
    """源相对路径（相对 src/，如 '<id>/image/截屏….png'）→ (build 相对路径, kind)。

    产物名 = md5(src_rel)[:16] + 新后缀，保留原 <id>/<子目录>/ 层级。
    """
    p = Path(src_rel)
    kind = classify(p.suffix)
    name = hashlib.md5(src_rel.encode("utf-8")).hexdigest()[:HASH_LEN] + _out_ext(kind, p.suffix)
    return (p.parent / name).as_posix(), kind
