"""doit 构建入口：src/ → build/src/（增量、并行）。任务逻辑见 pipeline/__init__.py。

用法（在仓库根，建议用 .venv）：
  doit              全量/增量构建（page → media → config → home → site → search）
  doit -n 2         并行（媒体编码受益最大）
  doit clean        删除所有产物
  doit list         列出任务组
  doit page         只构建正文；  doit "page:<id>" 单页
  doit media        只编码媒体
  doit config       toc.yaml → mkdocs.yml + 拷贝品牌 css/js + 主题覆盖 + logo 到 build/
  doit home         生成首页（hero + 卡片）
  doit site         mkdocs build → site/
  doit search       Pagefind 中文搜索索引 → site/pagefind/

增量仅为本地开发便利：doit 按输入文件时间戳/哈希跳过未变目标
（改一个 .md → 只重建该页；加一张图 → 只编码这一个文件）。
**不做源码指纹自动失效**——改了转换代码或编码参数后，自行 `doit clean`
（全部）或 `doit clean media` / `doit clean "page:<id>"`（局部）再重建。
否则「改一个 png 参数就重编码全部媒体」纯属灾难。CI 一律全新构建。
"""

# doit 从本模块命名空间发现 task_* 创建器；逻辑在 pipeline（规范化）与 ssg（mkdocs）包内。
from pipeline import task_page, task_media  # noqa: F401
from ssg import task_config, task_home, task_site, task_search  # noqa: F401

DOIT_CONFIG = {
    "default_tasks": ["page", "media", "config", "home", "site", "search"],
    "verbosity": 1,
}
# 提速可选：加 "check_file_uptodate": "timestamp"（按 mtime，免每次 md5 全量 2GB）；
# 但切换 checker 会让既有 .doit.db 失配而触发一次全量重编码，故默认保持 md5。
