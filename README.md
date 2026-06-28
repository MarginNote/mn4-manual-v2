# MarginNote 4 用户手册

MN4 用户手册：内容源是 wolai 导出的 Markdown（见 `src/`），经构建管线规范化、压缩后渲染为
可部署的静态站点。

## 结构

```
src/              内容源：每页一个 wolai-id 目录 + toc.yaml/synonyms.yaml/faq.yaml（撰写见 src/README.md）
pipeline/         构建管线：src/ 规范化 + 媒体压缩 → build/src（详见 pipeline/README.md）
dodo.py           doit 构建入口（导入 + 配置）
requirements.txt  构建依赖（另需系统 ffmpeg）
```

## 构建

```bash
virtualenv .venv
.venv/bin/pip install -r requirements.txt    # 另需系统 ffmpeg / ffprobe
.venv/bin/doit -n 2                           # src/ → build/src
```

## 文档

- 撰写 / 增改页面：[`src/README.md`](src/README.md)
- 构建管线：[`pipeline/README.md`](pipeline/README.md)
