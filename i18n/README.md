# i18n —— 英文版源（自包含）

英文版的全部源都在这里，与 `src/`（中文 wolai 导出）解耦：

```
i18n/en/
  <wolai-id>/index.md   每页英文译文（与 src/<id>/ 平行；预留 image/ 以便日后译图）
  toc.yaml              目录英文文案 overlay：sections/categories 以中文名为键、pages 以 id 为键
```

- 译文是**源文件**（纳入版本库），不是构建产物。
- 翻译术语参照 `../src/glossary.md`（中英术语表，wolai 导出，保持原样不结构化）。
- **slug**（英文 URL 目录名，中英共用）在 `../src/toc.yaml` 每页的 `slug` 字段——它是语言无关的
  页面标识，故留在 `toc.yaml`，不在本目录。
- 构建期：`pipeline.task_page_en` 把 `<id>/index.md` 落到 `build/src/<slug>/index.en.md`（并改写
  站内链接 id→slug）；`ssg.config.load_merged_toc()` 把 `toc.yaml` overlay **内存合并**进中文目录
  （`src/toc.yaml` 与本 `toc.yaml` 都不被改写）。

详见根 [`README`](../README.md) 的「i18n」一节与 [`ssg/README`](../ssg/README.md)「导航与 i18n」。
