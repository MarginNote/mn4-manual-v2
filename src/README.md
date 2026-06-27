# 内容源

MN4 手册是在 wolai 上撰写的，写完后导出为 markdown 并放到这里。这里存储内容源文件：

1. 每个页面一个目录，目录名为**该页的 wolai id**，内容为 wolai 导出的压缩包内容（markdown 正文 + 图片）
2. 目录结构 `toc.yaml` （section -> category -> page）

## 内容修改

1. 在 wolai 里把该页导出为 Markdown（注意选择**“生成目录”为“不生成”**），会得到一个 zip 文件
2. 解压 zip 到 `src/`，会得到一个目录（内含 `<标题>.md` 和 `image/`），将该目录改名为页面 URL `https://www.wolai.com/<id>` 中的 `<id>` 段
3. 按需改 `toc.yaml` （不在其中的页面不会发布）
