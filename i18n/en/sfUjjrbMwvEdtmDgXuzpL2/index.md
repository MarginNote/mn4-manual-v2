# Third-Party App Integration ①: Understanding Note Backlinks

> 💡MarginNote 4 can generate two kinds of dedicated URLs—card URLs and interface URLs—to enable cross-platform integration with third-party apps and make it easy to share and collaborate on notes.

## 1 Generate & Get URLs

### 1.1 Generate & Get a Note Card URL

The URL tied to the unique ID of each MarginNote 4 card is likewise supported in third-party software. It is also a low-level mechanism of Apple's operating system, commonly known as a URL Scheme.

How to get a card's URL:

1. Select a mind map card and press the shortcut `Shift+Command+C` to copy the current card's URL to the clipboard.
2. Open the card editor → … More → `Copy Card URL`

   ![Copy Card URL Copy Card URL ](image/6fda3b7e8d946fe5.webp)

### 1.2 Generate & Get an Interface URL

MarginNote 4 can also capture the frozen state of the current interface, which is distinct from a card URL. A card URL only jumps to a note's content, whereas an interface URL additionally preserves the user's window size, proportions, the state of each toggle, and even the default values of certain views—ensuring that the viewer's interface closely matches the one the original user sees after clicking the URL.

Interface URLs are commonly used for tutorial demonstrations: an instructor records an interface URL in a study set and shares it with learners, who can then use the URL to reach the same interface as the instructor.

Note, however, that if a learner already has their own view configuration, it will be overwritten by the instructor's default values and will then need to be readjusted. (The interface URLs used in the official tutorials detect the tutorial-reading state and restore the user's own configuration once the tutorial is finished.)

Getting the interface URL:
Press the shortcut `Command+Option+0` to copy the current interface URL to the clipboard.

![Copy the current URL state to the clipboard Copy the current URL state to the clipboard ](image/d965d7240c574723.webp)

## 2 Export and Open in Third-Party Apps

> 💡When you export to any of the supported formats, including Word and PDF, each one contains a MarginNote 4 hyperlink. Clicking the link in third-party software, or opening it via Safari, jumps the interface to the corresponding location in your MarginNote 4 notes, helping you recall the surrounding knowledge points.

![Export and open in other apps Export and open in other apps ](image/b1f8bdf08637a6ad.webp)

The example shows Word; other formats work similarly:

![MarginNote 4 hyperlink exported into Word MarginNote 4 hyperlink exported into Word ](image/36f4fd7afa6997f0.webp)

> 💡Your notes belong to you. Convert them into many formats and use the URL Scheme for two-way jumping, so that multiple apps can jump back and forth to the source text. Integrate with powerful tools such as DEVONthink, OmniOutliner, Tinderbox, Evernote, and OmniFocus to build your personal knowledge management system.
> 
> ![Build a personal knowledge management system](<https://faq.marginnote.cn/MarginNote3/MarginNote for Mac/Untitled 1.png> "建构个人知识管理系统")

A Note-Taking System — How to Use MarginNote3, DEVONThink3, TheBrain11, and nvALT as a Single App

[A Note-Taking System — How to Use MarginNote3, DEVONThink3, TheBrain11, and nvALT as a Single App\_bilibili\_bilibili https://github.com/John15263/note-taking-system, views 11178, danmaku 4, likes 111, coins 69, favorites 306, shares 46, video creator john15263, author bio , related videos: The First Step in John's Reading Workflow — Information Flows from MarginNote3 into nvALT, Spice and Weapons-1-Installing Marginnote, DEVONThink, K https://www.bilibili.com/video/av90220643/](https://www.bilibili.com/video/av90220643/ "一个笔记系统——如何把MarginNote3, DEVONThink3, TheBrain11 和 nvALT当一个App使用_哔哩哔哩_bilibili 视频播放量 11178、弹幕量 4、点赞数 111、投硬币枚数 69、收藏人数 306、转发人数 46, 视频作者 john15263, 作者简介 ，相关视频：John的阅读工作流的第一步——信息从MarginNote3流入nvALT，香料与武器-1-安装Marginnote，DEVONThink，K https://www.bilibili.com/video/av90220643/")

MarginNote and OmniFocus — How to Use MarginNote and OmniFocus for Reading-Task GTD

[ MarginNote and OmniFocus - How to Use MarginNote and OmniFocus for Reading-Task GTD\_bilibili\_bilibili Huangjinsheng 1.0: How to Use MarginNote and OmniFocus for Reading-Task GTD, views 1652, danmaku 0, likes 14, coins 2, favorites 24, shares 0, video creator john15263, author bio , related videos: The First Step in John's Reading Workflow — Information Flows from MarginNote3 into nvALT, MarginNote-DeepL, Spice and Weapons-1-Installing Marginnote, DEVONThi https://www.bilibili.com/video/av64216865/](https://www.bilibili.com/video/av64216865/ " MarginNote与OmniFocus-如何用MarginNote与OmniFocus进行阅读任务GTD_哔哩哔哩_bilibili 幌金绳1.0：如何用MarginNote与OmniFocus进行阅读任务GTD, 视频播放量 1652、弹幕量 0、点赞数 14、投硬币枚数 2、收藏人数 24、转发人数 0, 视频作者 john15263, 作者简介 ，相关视频：John的阅读工作流的第一步——信息从MarginNote3流入nvALT，MarginNote-DeepL，香料与武器-1-安装Marginnote，DEVONThi https://www.bilibili.com/video/av64216865/")

MarginNote and Typora - How to Write Reading Notes with MarginNote - 1.0 - How to Input Quickly

[MarginNote and Typora - How to Write Reading Notes with MarginNote - 1.0 - How to Input Quickly\_bilibili\_bilibili How to Write Reading Notes with MarginNote and Typora, views 1546, danmaku 0, likes 11, coins 4, favorites 18, shares 1, video creator john15263, author bio , related videos: MarginNote-DeepL, 【Readings】Why a Joke Stops Being Funny After Being Repeated Too Many Times, Little John Update: Moving Web Pages into MarginNote, How to Read English Papers Elegantly | Kumārajīva (Auto-Translate) and Key https://www.bilibili.com/video/av63440619/](https://www.bilibili.com/video/av63440619/ "MarginNote与Typora-如何用MarginNote写读书笔记-1.0-如何快速输入_哔哩哔哩_bilibili 如何使用MarginNote和Typora写读书笔记, 视频播放量 1546、弹幕量 0、点赞数 11、投硬币枚数 4、收藏人数 18、转发人数 1, 视频作者 john15263, 作者简介 ，相关视频：MarginNote-DeepL，【Readings读物】为什么一个笑话重复很多遍就不好笑了，小约翰更新：搬运网页到MarginNote，如何优雅地阅读英文论文 | 鸠摩罗什（自动翻译）与Key https://www.bilibili.com/video/av63440619/")

Keyboard Maestro — Marginnote Power Tricks

[ Marginnote Power Tricks\_bilibili\_bilibili Marginnote Power Tricks contains 8 videos in total, including: New Pasteboard, New Macro, Copy Content\&Link, and more. For more great videos from this uploader, please follow the uploader's account. https://www.bilibili.com/video/av27670825/](https://www.bilibili.com/video/av27670825/ " Marginnote骚操作_哔哩哔哩_bilibili Marginnote骚操作共计8条视频，包括：新建粘贴板、新建Macro、Copy Content&Link等，UP主更多精彩视频，请关注UP账号。 https://www.bilibili.com/video/av27670825/")

## 3 Cross-App Note-Syncing Plugins

Taking the Obsidian and Flomo plugins as examples, a note card is created simultaneously across two or more apps, each also carrying a globally available context backlink.

[ 【Third-Party MN Plugin】Obsidian-Bridge (Dynamic Markdown Export) — Connecting Two Knowledge Galaxies #Ver.3.0.0 Officially Signed# - Plugin Release Area｜Unrestricted editing and updating of the main post allowed - MarginNote Chinese Community Obsidian BridgeObsidian Bridge plugin builds a bridge from MarginNote to Obsidian. Through it, we can import the writing material and creative inspiration accumulated in MarginNote into Obsidian, using Ma\&hellip; https://bbs.marginnote.com.cn/t/topic/21235](https://bbs.marginnote.com.cn/t/topic/21235 " 【第三方MN插件】Obsidian-Bridge（Markdown动态导出）——连接两个知识星球 #Ver.3.0.0 已获官方签名# - 插件发布区｜允许不受限制地编辑更新主帖 - MarginNote 中文社区 Obsidian BridgeObsidian Bridge 插件架起了 MarginNote 通往 Obsidian 的桥梁，通过它，我们可以把在 MarginNote 中积累的写作素材/创作灵感导入到 Obsidian 中，使用 Ma… https://bbs.marginnote.com.cn/t/topic/21235")

[ 【Third-Party MN Plugin】I wrote a flomo plugin—is anyone using flomo? #Ver.0.0.2 Officially Signed# - Plugin Release Area｜Unrestricted editing and updating of the main post allowed - MarginNote Chinese Community The v 0.0.2 release adds the following support: support for switching flomo's position (mainly referencing deepl's code; I'd like to ask how to refresh the position directly—currently it takes effect only after toggling the plugin off and on again). Notes now include a note id, in preparation for opening marginNote. Preview image    \&hellip; https://bbs.marginnote.com.cn/t/topic/18381](https://bbs.marginnote.com.cn/t/topic/18381 " 【第三方MN插件】写了个flomo的插件，有在用flomo的同学吗 #Ver.0.0.2 已获官方签名# - 插件发布区｜允许不受限制地编辑更新主帖 - MarginNote 中文社区 v 0.0.2版本发布做了以下支持 支持切换flomo的位置(主要参考deepl的代码，想请教下怎么直接刷新位置，现在是再次开关插件后生效) 笔记增加了笔记id ,为打开marginNote做准备 预览图    … https://bbs.marginnote.com.cn/t/topic/18381")

## 4 Apple Script

Coming Soon

AppleScript automation and JavaScript plugin extensions enhance MN's integration with many professional research tools, enabling uses such as data conversion, advanced export, automatic card-creation rules, and function computation.

The latest Apple Script rules and syntax supported by MarginNote 4 can all be looked up through the dictionary feature of the system's built-in app, "Script Editor."

![](image/e6d2883d426b3ad0.webp)

![](image/4324c0c7d8deb9db.webp)

![](image/7f42d062aed8cedb.webp)
