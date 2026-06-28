"""format_media.py —— ffmpeg 媒体编码（一次处理一个文件）。

kind（来自 assets.classify）：
  webp       —— png/jpg/jpeg → 静态 webp（q80, ≤1200px, lanczos, -m 4）
  webp_anim  —— gif / 视频 → 动画 webp（libwebp_anim, loop 0, q60, ≤1200px,
                帧率：原 ≤12fps 保留，否则降到 10fps）—— 参数对齐旧仓库 compress_media.py
  copy       —— 其它（如 .ttf）原样复制

源始终来自只读的 src/；产物写到 build/。注意：doit 只按**源文件**判定 uptodate，
不跟踪本文件参数——改了编码参数后需自行 `doit forget media` / `doit clean` 再构建。
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

WIDTH_CAP = 1200             # 最长边上限（静态图与动图统一，对齐旧仓库）
IMAGE_QUALITY = 80           # 静态 webp -q:v
ANIM_QUALITY = 60            # 动画 webp -q:v
WEBP_COMPRESSION = 4         # libwebp -m（4=默认；比 6 快很多，体积只大约 5%）
ANIM_FPS_THRESHOLD = 12      # 原帧率 ≤ 此值保留
ANIM_FPS_TARGET = 10         # 否则降到此帧率


def _ffmpeg(args: list[str]) -> None:
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", *args],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True,
    )


def media_fps(path) -> float:
    try:
        out = subprocess.check_output(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", str(path)],
            text=True,
        ).strip()
        num, den = out.split("/")
        return int(num) / int(den) if int(den) else 0.0
    except Exception:  # noqa: BLE001
        return 0.0


def encode(src, dst, kind: str) -> bool:
    """把 src 编码/复制到 dst（按 kind）。成功返回 True，失败抛异常（供 doit 标记失败）。"""
    src, dst = Path(src), Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    # 临时名把 .__tmp__ 放在真实后缀之前，确保 ffmpeg 仍能按扩展名推断输出格式
    tmp = dst.with_name(dst.stem + ".__tmp__" + dst.suffix)

    if kind == "copy":
        shutil.copy2(src, dst)
        return True

    scale = f"scale='min({WIDTH_CAP},iw)':-2:flags=lanczos"
    if kind == "webp":
        args = ["-i", str(src), "-vf", scale, "-c:v", "libwebp",
                "-q:v", str(IMAGE_QUALITY), "-compression_level", str(WEBP_COMPRESSION), str(tmp)]
    elif kind == "webp_anim":                        # gif / 视频 → 循环动画 webp
        fps = media_fps(src)
        target = fps if 0 < fps <= ANIM_FPS_THRESHOLD else ANIM_FPS_TARGET
        args = ["-i", str(src), "-an", "-vf", f"{scale},fps={target:g}",
                "-c:v", "libwebp_anim", "-loop", "0",
                "-q:v", str(ANIM_QUALITY), "-compression_level", str(WEBP_COMPRESSION), str(tmp)]
    else:
        raise ValueError(f"unknown kind {kind!r}")

    try:
        _ffmpeg(args)
        os.replace(tmp, dst)
    except Exception:
        if tmp.exists():
            tmp.unlink(missing_ok=True)
        raise
    return True
