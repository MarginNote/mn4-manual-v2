"""format_media.py —— ffmpeg 媒体编码（一次处理一个文件）。

kind（来自 assets.classify）：
  webp      —— png/jpg/jpeg → webp（q80, ≤1200px, lanczos）
  mp4_gif   —— gif → mp4（h264/yuv420p/faststart, crf28, ≤1200px,
               帧率：原 ≤12fps 保留，否则降到 10fps）
  mp4_video —— mp4/mov/… → mp4（h264, crf26, ≤1280px, 帧率封顶 30fps）
  copy      —— 其它（如 .ttf）原样复制

源始终来自只读的 src/；产物写到 build/。改这里的参数会改变本文件内容，
dodo 用文件哈希做 doit 的 uptodate，故参数变更会自动触发相关媒体重新编码。
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

IMG_WIDTH_CAP = 1200          # 静态图 / gif 最长边上限
VID_WIDTH_CAP = 1280          # 视频最长边上限
WEBP_QUALITY = 80
WEBP_COMPRESSION = 4
GIF_MP4_CRF = 28
VIDEO_MP4_CRF = 26
X264_PRESET = "medium"
ANIM_FPS_THRESHOLD = 12       # gif 原帧率 ≤ 此值保留
ANIM_FPS_TARGET = 10          # 否则降到此帧率
VIDEO_FPS_CAP = 30            # 真实视频帧率封顶


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

    scale = f"scale='min({IMG_WIDTH_CAP},iw)':-2:flags=lanczos"
    if kind == "webp":
        args = ["-i", str(src), "-vf", scale, "-c:v", "libwebp",
                "-q:v", str(WEBP_QUALITY), "-compression_level", str(WEBP_COMPRESSION), str(tmp)]
    elif kind == "mp4_gif":
        fps = media_fps(src)
        target = fps if 0 < fps <= ANIM_FPS_THRESHOLD else ANIM_FPS_TARGET
        args = ["-i", str(src), "-movflags", "+faststart", "-pix_fmt", "yuv420p",
                "-vf", f"{scale},fps={target:g}",
                "-c:v", "libx264", "-preset", X264_PRESET, "-crf", str(GIF_MP4_CRF),
                "-an", str(tmp)]
    elif kind == "mp4_video":
        fps = media_fps(src)
        target = min(fps, VIDEO_FPS_CAP) if fps > 0 else VIDEO_FPS_CAP
        args = ["-i", str(src), "-movflags", "+faststart", "-pix_fmt", "yuv420p",
                "-vf", f"scale='min({VID_WIDTH_CAP},iw)':-2:flags=lanczos,fps={target:g}",
                "-c:v", "libx264", "-preset", X264_PRESET, "-crf", str(VIDEO_MP4_CRF),
                "-c:a", "aac", "-b:a", "96k", str(tmp)]
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
