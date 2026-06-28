"""项目级配置（当前：路径布局）。

叶子模块：只依赖标准库，被 pipeline / ssg 共同 import，自身不 import 它们 —— 从而两包
解耦，仅经 build/src 这一目录契约交接。（也因此不能放进 dodo.py：dodo import 两包，
否则成环。）后续其它配置（域名、部署参数等）也放这里。

路径可用环境变量覆盖：
  MN_ROOT   仓库根（默认当前目录）
  MN_BUILD  产物根（默认 build）
"""

import os
from pathlib import Path

ROOT = Path(os.environ.get("MN_ROOT", "."))
SRC = ROOT / "src"                                    # 内容源
BUILD = ROOT / os.environ.get("MN_BUILD", "build")    # 所有生成物的根
BUILD_SRC = BUILD / "src"                             # 规范化产物 = SSG 的 docs_dir（两阶段契约）
SITE = BUILD / "site"                                 # mkdocs 站点输出
MKDOCS_YML = BUILD / "mkdocs.yml"                      # 生成的 mkdocs 配置
OVERRIDES = BUILD / "overrides"                        # 生成的 Material 主题覆盖目录（custom_dir）
TOC = SRC / "toc.yaml"                                # 目录结构（发布集）

# 部署/展示配置（非路径）
SITE_URL = os.environ.get("MN_SITE_URL", "https://manual.marginnote.com.cn/")
SITE_DESCRIPTION = (
    "MarginNote 4 用户手册——智能学习软件 PDF、笔记、脑图深度学习的完整指南。"
    "涵盖文档笔记、脑图、卡片复习、AI 功能与高级技巧。"
)
