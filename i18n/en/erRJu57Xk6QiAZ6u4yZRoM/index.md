# Export Documents, Mind Maps, and Study Sets

> 💡This page mainly explains how to export PDFs, mind maps, and study sets for sharing. For exports related to document backup and note backup, see [Data Sync, Backup & Restore](../qU6nwa4s6GCBuTDsjs9oeu/index.md)

> 💡**Quick jump to common scenarios**
> 1\. Export a PDF with notes: Export Flattened PDF (with notes)
> 2\. Export the full mind map / outline list as PDF: Export Mind Map as PDF
> 3\. Export part of the mind map / outline list as PDF: Export Mind Map as PDF (Focus Branch)

## 1 Export

### 1.1 Documents

#### 1.1.1 Source PDF (without notes)

When you need to export the original document, tap the "..." More button at the bottom-right of the document, then tap "Export Source PDF File" in the submenu that pops up

![Animated demo: Export Source PDF File Animated demo: Export Source PDF File ](image/9d4d0864a80a514a.webp)

#### 1.1.2 Export Flattened PDF (with notes)

When you need to export a document that contains notes, there are two ways:

1. Tap the `Document - More` button at the top-right of the document view, then tap `Export Document as Flattened PDF` to export the document as a flattened PDF or a long image

![](image/732a1adbe0fea2df.webp)

1. Tap `Study Set - More` - `Export Study Set - Export Document as Flattened PDF` at the top-right of the study set view

![](image/6f7e64e532c13d45.webp)

> 💡The notes in an exported flattened PDF cannot be edited in any software (including MarginNote), and exported flattened PDFs currently do not include the table of contents created in MarginNote

### 1.2 Mind Map

#### 1.2.1 Export Mind Map as PDF

> 💡The exported PDF shows the mind map/outline at its current expansion state, so to display all content **you must expand all levels**

1. Tap `Study Set - More`

![](image/49ebd2a67e979070.webp)

2.Tap `Export Mind Map as PDF`

![](image/6f7e64e532c13d45.webp)

1. Select `Export Mind Map` and `Export Card Outline`
   > 💡The exported PDF shows the mind map/outline at its current expansion state, so to display all content **you must expand all levels**![The card outline is a linear output, similar to a document The card outline is a linear output, similar to a document ](image/dd320c563e5d21f4.webp)
   > Select the content to export, tap `Export`, then choose to print or export to another app in the mind map PDF preview screen.

#### 1.2.2 Export Mind Map as PDF (Focus Branch)

> 💡When you only need to export part of the mind map, you can choose to export just the focus branch

1. First enter Focus mode on the top-level card of the branch you want to export (for the specific way to enter focus, see [Mind Map Focus](../5nntHuyzfBSdVrEo4YYhxC/index.md))
2. Tap `Study Set - More` - `Export Study Set`

![](image/49ebd2a67e979070.webp)

1. Tap `Focus Branch` - `Export Mind Map as PDF`; the remaining steps and notes are the same as Export Mind Map as PDF

   ![](image/2aab73ca788ce360.webp)

### 1.3 Study Set

Tap `Study Set - More` - `Export Study Set`

![](image/bcf78590c802b365.webp)

Under the `Export Backup` tab there are `Export Study Set Backup` and `Export to Note Database`

1. `Export Study Set Backup`: exports all document and note data of the current study set for sharing or backup; the backup file can only be opened with MarginNote
2. `Export to Note Database`: an exclusive feature of multi-note-database Max. By exporting some study sets to another note database, you can conveniently move study sets between databases, which is useful for isolating note data across different periods and different fields.
   > 💡For how to use note databases and common scenarios, see [Note Database ①: Creating and Managing Databases](../wVmpipXpgJM4ZicKDvV6A7/index.md)

### 1.4 Export to Other Formats

> 💡When exporting to other formats, you can also choose to export only the focus branch; the steps are the same as Export Mind Map as PDF (Focus Branch)

1. Tap `Study Set - More` - `Export Study Set`
2. You can export to the following formats: OmniOutliner (oo3), MindManager and iThoughts (mmap), Evernote (api), MS Word (docx), Anki (apkg)

> 💡Cards created with [Markdown and Formulas](../eShEtotNTstcUnT6o3FLAP/index.md) will not render correctly after export in software that does not support Markdown syntax

#### 1.4.1 Export to OmniOutliner (oo3)

1. Tap this option and choose whether to include excerpt colors when exporting the outline.
2.  An oo3 file is generated; import it using OmniOutliner, which supports the oo3 file format.

> 💡Tip: this file is located in the ExportedOmniOutlinerFiles folder within MarginNote 4's local folder.

![How the sample study set appears in OmniOutliner 4. How the sample study set appears in OmniOutliner 4. ](image/bf724b66d0b990b4.webp)

> 💡Tip: OmniOutliner's editing features require a subscription and are fairly expensive. You can tap the More Options after the file name in the top-left corner - Export As, to convert to more file formats.
> 
> ![  ](image/c0f3e8b4fff42c0e.webp)

#### 1.4.2 Export to MindManager and iThoughts (mmap)

1. Tap this option. You can choose whether to add MarginNote links to the exported mind map; if you do, you can tap a link to jump back to the corresponding card location in MarginNote

   ![](image/b39ba00ad156adcf.webp)
2. An mmap file is generated; import it with software that supports the mmap format.
   > 💡Tip: this file is also located in MarginNote 4's local folder.
3. Software that supports the mmap format:
   1. MindManager

      ![How the sample study set appears in MindManager. How the sample study set appears in MindManager. ](image/a979f432af00bc38.webp)
      > 💡MindManager Go in the App Store can only view mmap files
   2. iThoughts

      ![How the sample study set appears in iThoughts. How the sample study set appears in iThoughts. ](image/3182053e0a45113d.webp)
      > 💡Tip: iThoughts can convert mind maps to many formats; among them, files in mm, opml, and xmind formats can be imported into Mubu (must be under 2 MB). Mubu lets you view mind maps/outlines synced across all platforms and devices. You can export the Mubu file, convert it back to an mmap file via iThoughts, and import it back into MarginNote 4, choosing either to append it to an existing study set's mind map or to create a new mind map.
      > 
      > ⚠️iThoughts is no longer available for download in the App Store; Mac and Windows users can find the iThoughts installer on their own.
      > 
      > ![  ](image/41a56d9850f08c34.webp)
   3. MindNode

      ![How the sample study set appears in MindNode. How the sample study set appears in MindNode. ](image/f802c2bbae318118.webp)
      > 💡Tip: MindNode can convert the mind map format into the formats shown.
      > 
      > ![  ](image/e08365b598018d71.webp)
   4. MindMaster (under 10 MB)
   5. Baidu Naotu
   6. Xmind (non-mobile version)

#### 1.4.3 Export to Evernote (api)

1. Tap this option, log in to Evernote (Yinxiang Biji), choose the target folder, and tap Import.

   ![](image/cfb6752a81b49544.webp)
2. Choose whether to attach the documents associated with the cards.
3. Choose whether to attach the mind map.
4. The study set will be exported in the background, and you will receive a notification when it finishes.

#### 1.4.4 Export to MS Word (docx)

1. Tap this option and choose whether to include excerpt colors when exporting the outline.
2. A docx file is generated; import it with software that supports docx.

> 💡Tip: this file is located in MarginNote 4's local folder.

![Display is abnormal in software such as WPS and Shimo Docs; open the file with Microsoft Word or Pages Display is abnormal in software such as WPS and Shimo Docs; open the file with Microsoft Word or Pages ](image/1b958a49c5072922.webp)

#### 1.4.5 Export to Anki (apkg)

After tapping this option, the dialog shown appears. Besides exporting cards, the default template also offers the following export settings

![](image/018c0cd3b692c696.webp)

1. `Export link to MarginNote`

   ![Exports the card's URL; this link jumps to the card's location in the MarginNote mind map. Exports the card's URL; this link jumps to the card's location in the MarginNote mind map. ](image/b95a678d5156bdae.webp)
2. `Export sub-links as images`

![Exports all child nodes of the card as images. Exports all child nodes of the card as images. ](image/3315032b31b62153.webp)

1. `Export voice comments`

![Exports the voice comments on the card. Exports the voice comments on the card. ](image/f754af9187a86cc9.webp)

`Export multiple Anki cards for the multiple image clozes on a single MN card`: when a single review card has multiple clozes, a corresponding number of Anki cards will be generated

1. `Hide All, Show One`

   ![Front side Front side ](image/ecbab2915b22e1a7.webp)

   ![Back side Back side ](image/40f4d8b2499ef2b1.webp)
2. `Hide All, Show All`

   ![Front side Front side ](image/bfaf4470033a7f7a.webp)

   ![Back side Back side ](image/5f4fbadc99dc5c83.webp)
3. `Hide One, Show One`

   ![Front side Front side ](image/d2e1f0b6c930cab9.webp)

   ![Back side Back side ](image/c2c7554de55c562c.webp)

> 💡For advanced usage of custom templates, see [Flashcard Review ③: Export to Anki & Template Configuration](../4zZ4C4Y4jgfdszohqSE4Zm/index.md)

## 2 Other Note-Export Plugins

> 💡Plugins on the MarginNote forum also support exporting study sets to more third-party apps, such as Obsidian and flomo; visit the forum to learn more.

[Third-Party App Integration ②: Obsidian + MN4](../hTKcNyLnc362NvwEvMbt2e/index.md)

[ [Third-Party MN Plugin] Obsidian-Bridge (Dynamic Markdown Export) — Bridging Two Knowledge Worlds #Ver.3.0.0 Officially Signed# - #162, by Deanlzy - Plugin Release Area｜Unrestricted editing and updating of the main post allowed - MarginNote Chinese Community Obsidian BridgeObsidian Bridge plugin builds a bridge from MarginNote to Obsidian. Through it, we can import the writing material / creative inspiration accumulated in MarginNote into Obsidian, using Ma\&hellip; https://bbs.marginnote.com.cn/t/topic/21235/162](https://bbs.marginnote.com.cn/t/topic/21235/162 " 【第三方MN插件】Obsidian-Bridge（Markdown动态导出）——连接两个知识星球 #Ver.3.0.0 已获官方签名# - #162，来自 Deanlzy - 插件发布区｜允许不受限制地编辑更新主帖 - MarginNote 中文社区 Obsidian BridgeObsidian Bridge 插件架起了 MarginNote 通往 Obsidian 的桥梁，通过它，我们可以把在 MarginNote 中积累的写作素材/创作灵感导入到 Obsidian 中，使用 Ma… https://bbs.marginnote.com.cn/t/topic/21235/162")

[ [Third-Party MN Plugin] I wrote a flomo plugin — is anyone here using flomo? #Ver.0.0.2 Officially Signed# - Plugin Release Area｜Unrestricted editing and updating of the main post allowed - MarginNote Chinese Community The v0.0.2 release adds the following support: support for switching flomo's location (mainly referencing deepl's code; I'd like to ask how to refresh the location directly — currently it only takes effect after toggling the plugin off and on again) notes now include a note id, in preparation for opening marginNote preview image    \&hellip; https://bbs.marginnote.com.cn/t/topic/18381](https://bbs.marginnote.com.cn/t/topic/18381 " 【第三方MN插件】写了个flomo的插件，有在用flomo的同学吗 #Ver.0.0.2 已获官方签名# - 插件发布区｜允许不受限制地编辑更新主帖 - MarginNote 中文社区 v 0.0.2版本发布做了以下支持 支持切换flomo的位置(主要参考deepl的代码，想请教下怎么直接刷新位置，现在是再次开关插件后生效) 笔记增加了笔记id ,为打开marginNote做准备 预览图    … https://bbs.marginnote.com.cn/t/topic/18381")
