# Flashcard Review ③: Export to Anki & Template Configuration

> 💡 Flashcard series navigation
> 
> Creating flashcards: [Creating Flashcards ①: Getting to Know Flashcards and Review Card Decks](../auMvW4AbuCoxDmYipisYoS/index.md)[Creating Flashcards ②: Adding Cards to a Review Card Deck](../pKZaNAWQAm3Wp41awj1ZJb/index.md)[Creating Flashcards ③: Setting the Flashcard Front and Back](../pBH9BFrgyZgeWJVf3xLyVA/index.md)
> 
> Scientific review: [Flashcard Review ①: Scientific Review Based on the FSRS Anti-Forgetting Algorithm](../31KwWufHLt8MUbyxQahbP3/index.md)[Flashcard Review ②: Tracing Source Context](../ozYBXbvi3AkqiBShA7X7Co/index.md)Flashcard Review ③: Export to Anki & Template Configuration
> 
> - If reviewing within MN is already efficient enough for you, you can keep using the Flashcard Review ①② workflow;
> - If you need more granular review, read this article in detail: Export to Anki.

> 💡 Once you have finished creating note cards in MarginNote but want **more refined review management and richer template styles**, exporting your cards to Anki may be the better choice.
> 
> ![Export to Anki Export to Anki ](image/82e3e819b0ca2656.webp)

## 1 Before Exporting: Settings Related to "Cloze"

In full-screen review mode → tap the "… More" button on the right side of the toolbar → choose different cloze effects according to your needs:

![](image/18439b7a64c0d3bb.webp)

### 1.1 Cloze Highlighters

![Cloze highlighters on the document Cloze highlighters on the document ](image/0e5370fc0e3571df.webp)

![Cloze highlighters on the card Cloze highlighters on the card ](image/91481a76c9c3df0f.webp)

### 1.2 Cloze Emphasize/Cloze

![Animated demo: clozing emphasized text Animated demo: clozing emphasized text ](image/a5d2d499e89f75d9.webp)

![Animated demo: clozing emphasis in an image Animated demo: clozing emphasis in an image ](image/1558dc547a75726c.webp)

## 2 How to "Export to Anki"?

- Method 1: Export from "Review Card Decks" on the home page

  Review Card Decks → select a card deck → Export → Export to Anki (apkg)

  ![](image/bf8986933b3cc88c.webp)
- Method 2: Export from "Review" in a study set

  Review → … (More) → Export to Anki (apkg)

  ![](image/722d11b640d6efa3.webp)
- Method 3: Export from "More" in a study set

   … (More) → Export Study Set → Export to Anki (apkg)

  ![](image/d92aa5a1684e5b5a.webp)

## 3 Exporting: Using the "Default Template"

![Default template Default template ](image/6ffd1dc325ee9ff7.webp)

For pure memorization review, just use the default template and export the basic question-and-answer fields.

### **Export Link to MarginNote**

When you need to backlink for verification, check "Export Link to MarginNote": this exports the card's URL, which lets you jump to the card's location in the MarginNote mind map.

![Export link to MarginNote Export link to MarginNote ](image/6391bd356e5507b0.webp)

### **Export Child Links as Images**

When you need to review your knowledge network, check "Export Child Links as Images": this exports all of the card's child nodes as images.

![Export child links as images Export child links as images ](image/822cac723b23c54a.webp)

### **Export Voice Comments**

For auditory review, check "Export Voice Comments": this exports the voice comments on the card.

![Export voice comments Export voice comments ](image/a3fa0da7e7264af1.webp)

### **Export Multiple Anki Cards for Multiple Image Clozes on One MN Card**

Hide all, reveal one

![Hide all, reveal one — front Hide all, reveal one — front ](image/b4c929f74601e2cf.webp)

![Hide all, reveal one — back Hide all, reveal one — back ](image/2ad227dc9d0171e7.webp)

Hide all, reveal all

![Hide all, reveal all — front Hide all, reveal all — front ](image/e7f25e2db0d149c6.webp)

![Hide all, reveal all — back Hide all, reveal all — back ](image/3daf90f211d9d5cb.webp)

Hide one, reveal one

![Hide one, reveal one — front Hide one, reveal one — front ](image/35db559c3075cc7f.webp)

![Hide one, reveal one — back Hide one, reveal one — back ](image/368c0b6a0a746b5d.webp)

## 4 Exporting: Using a "Custom Template"

![Basic 3in1 custom template Basic 3in1 custom template ](image/c509169435c1119b.webp)

- What each note card data field means
  | MarginNote Card Data | Field | Meaning |
  | ------------------ | ------------- | -------------------------------- |
  | MarginNote card front (question) | #CardQuestion | The front of the card |
  | MarginNote card back (notes) | #NoteWhole | The back of the card (i.e. **all notes on the card**) |
  | Card title section | #NoteTitle | The card's title |
  | Card excerpt section | #NoteExcerpt | The card's excerpt (a **sourced note** excerpted from the document) |
  | Card comment section | #NoteComment | The card's comments (including tags and voice comments) |
  | Remark (for search) | #Remark | All text content on the card (including OCR results), so it can be searched in Anki |
  | MarginNote backlink | #MNLink | This link jumps to the card's location in the MarginNote mind map |
  | Child node links | #MapLink | The card's child nodes, which can generate image previews in Anki |
- Detailed illustration of note card data
  - Front (question) and back (card content)
    - MarginNote card front (question)

      ![MarginNote card front (question) MarginNote card front (question) ](image/5459a7c089807ed7.webp)
    - MarginNote card back (notes)

      ![MarginNote card back (notes) MarginNote card back (notes) ](image/fc6f84e29f6c1374.webp)
  - The card's title, excerpt, and comments
    - Card title section

      ![Card title section Card title section ](image/9086d9aec266771e.webp)
      > 💡 When a card has no title, its first excerpt is treated as the card's title.
    - Card excerpt section

      ![Card excerpt section Card excerpt section ](image/b868c30d3e7bc5d6.webp)
    - Card comment section

      ![Card comment section Card comment section ](image/99e164a646d88d82.webp)
      > 💡 Tags also count as part of the comment section.

> 💡 To achieve recall-based review, the "cloze/cloze/emphasize" on a card must be placed on the front of the card. (Content is pulled from the back of the card to serve as the question on the front of the flashcard.)

### 4.1 How to Use a Custom Template?

- Steps for using a custom template (using the "Basic 3in1 template" as an example)
  - First, save the "Basic 3in1 template" to "Local Files"
  - When exporting, switch to "Custom Template" → tap "Select Template ( \*.apkg)" → choose the custom template you saved to "Local Files"

    ![](image/6ff5999636d88599.webp)
  - From the field list, select the MarginNote card data you want and map it to the Anki fields

    ![](image/a99c01b2b8884453.webp)
  - Select Anki → tap "Import" in the top-right corner

    ![](image/a8ed74c5d736458a.webp)

> 💡 If you want to use the "Export Link to MarginNote", "Export Child Links as Images", or "Export Voice Comments" note data in a custom template, you must first check the corresponding export options during the default-template step in order to export them!

### 4.2 Downloading Custom Templates

- MN3 xiamu template

  [ MN3 + Anki integration: sharing my modified Anki template for MarginNote3 - Anki Zone——Memory Palace - MarginNote Chinese Community Overall, only the CSS styling was changed from the original; the core fields and the front/back code were left unmodified, which avoids conflicts. Text-box width, font size, spacing, and line height were adjusted so the result looks better on large computer screens. The colors of bold, underline, and italic text were changed. Changed cl\&hellip; https://bbs.marginnote.com.cn/t/topic/2964](https://bbs.marginnote.com.cn/t/topic/2964 " MN3联动Anki：分享我修改的Marginnote3的Anki模板 - Anki专区——记忆宫殿 - MarginNote 中文社区 总体上仅在原来的基础上改动了CSS样式，作为核心的字段和正反面的代码没有修改，这样可以避免发生冲突。 调整了文本框宽度、字体大小、间距、行高，改动后呈现效果更适合大屏幕的电脑 改变了粗体、下划线、斜体的颜色 改变了cl… https://bbs.marginnote.com.cn/t/topic/2964")
- Basic 3in1 template

  【basic 3in1 | Random reset, Markdown cloze, keyboard shortcuts, read-aloud | All-in-one template optimization-Bilibili】 

  [ basic 3in1 | Random reset, Markdown cloze, keyboard shortcuts, read-aloud | All-in-one template optimization\_Bilibili\_bilibili 《 basic 3in1 》 The optimized version of the all-in-one template～ adds cloze/random reset, Markdown cloze, keyboard shortcuts, and text read-aloud… fixes the text-duplication issue mentioned in earlier episodes; adds table styling. Addendum ①: BV1q5411m7Xa Addendum ②: BV1DB4y1q7gd Table cloze: BV1bS4y1c76c OneNote nested-table cloze: BV1uU4y1m7nA Link: https://pan.baidu.com/s/1SyMSSpr4F1oTlh https://www.bilibili.com/video/BV1ZV4y1J7Dn/?buvid=XU69945620C34231F92B351C4D695FA793D76\&from\_spmid=main.space-contribution.0.0\&is\_story\_h5=false\&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D\&p=1\&plat\_id=116\&share\_from=ugc\&share\_medium=android\&share\_plat=android\&share\_session\_id=91b4db39-7cc1-4a1e-b767-12877bc5f33f\&share\_source=COPY\&share\_tag=s\_i\&spmid=united.player-video-detail.0.0\&timestamp=1714733842\&unique\_k=WgAcsf0\&up\_id=233956865](https://www.bilibili.com/video/BV1ZV4y1J7Dn/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=main.space-contribution.0.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=91b4db39-7cc1-4a1e-b767-12877bc5f33f&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733842&unique_k=WgAcsf0&up_id=233956865 " basic 3in1 | 随机重置、Markdown挖空、快捷键、朗读 | 三合一模板优化_哔哩哔哩_bilibili 《 basic 3in1 》三合一模板优化版本～新增填空/随机重置、Markdown挖空、快捷键、文本朗读…修改了前几期提到的文本重复问题；加入了表格样式。补充说明①：BV1q5411m7Xa补充说明②：BV1DB4y1q7gd表格挖空：BV1bS4y1c76cOneNote 嵌套表格挖空：BV1uU4y1m7nA链接：https://pan.baidu.com/s/1SyMSSpr4F1oTlh https://www.bilibili.com/video/BV1ZV4y1J7Dn/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=main.space-contribution.0.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=91b4db39-7cc1-4a1e-b767-12877bc5f33f&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733842&unique_k=WgAcsf0&up_id=233956865")
- Type 3in1 template

  【type 3in1 | Shortcuts/plugin | {{type:cloze:字段}} | All-in-one template optimization-Bilibili】 

  [ type 3in1 | Shortcuts/plugin | {{type:cloze:字段}} | All-in-one template optimization\_Bilibili\_bilibili Link: https://pan.baidu.com/s/19FB16QWvO0Ru-awPqkf\_Zw?pwd=x1r1 Access code: x1r1 【Shortcuts】 c1 replace https://www.icloud.com/shortcuts/20abecf2c59d4b3b90b43842ca8a09c2 【Customize Keyboard Shortcuts】 plugin code: 24411424 https://ankiw https://www.bilibili.com/video/BV1eB4y1k7vn/?buvid=XU69945620C34231F92B351C4D695FA793D76\&from\_spmid=main.space-contribution.0.0\&is\_story\_h5=false\&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D\&p=1\&plat\_id=116\&share\_from=ugc\&share\_medium=android\&share\_plat=android\&share\_session\_id=488db363-2be8-4066-a090-d6c01501dcbf\&share\_source=COPY\&share\_tag=s\_i\&spmid=united.player-video-detail.0.0\&timestamp=1714733857\&unique\_k=YSURNae\&up\_id=233956865](https://www.bilibili.com/video/BV1eB4y1k7vn/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=main.space-contribution.0.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=488db363-2be8-4066-a090-d6c01501dcbf&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733857&unique_k=YSURNae&up_id=233956865 " type 3in1 | 快捷指令/插件 | {{type:cloze:字段}} | 三合一模板优化_哔哩哔哩_bilibili 链接:https://pan.baidu.com/s/19FB16QWvO0Ru-awPqkf_Zw?pwd=x1r1 提取码:x1r1【快捷指令】 c1替换https://www.icloud.com/shortcuts/20abecf2c59d4b3b90b43842ca8a09c2【Customize Keyboard Shortcuts】插件代码：24411424https://ankiw https://www.bilibili.com/video/BV1eB4y1k7vn/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=main.space-contribution.0.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=488db363-2be8-4066-a090-d6c01501dcbf&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733857&unique_k=YSURNae&up_id=233956865")
- Word pronunciation template

  【Anki auto-pronunciation template | MarginNote card creation | universal for iOS / Android / PC-Bilibili】

  [ Anki auto-pronunciation template | MarginNote card creation | universal for iOS / Android / PC\_Bilibili\_bilibili This template uses automatic / online pronunciation; the deck file is small and easy to sync and transfer, and works across iOS / Android / PC. Choose one of the two templates and import it into Anki; when exporting from MN, please use the template in the 【dedicated】 folder; on OS15, TTS may not pronounce automatically, so we recommend the \<audio> "universal" template; on Android, TTS pronunciation is used, and some devices may also need to download the " Google Text-to-Speech Engine" to work. You can change it to American / British pronunciation yourself, video playback https://www.bilibili.com/video/BV1yU4y1f73i/?buvid=Y8470B823E0F865B46FD815AF771E428155B\&from\_spmid=main.space-contribution.0.0\&is\_story\_h5=false\&mid=e%2FMUnAJwgZE4We6tzMXcpg%3D%3D\&p=1\&plat\_id=315\&share\_from=ugc\&share\_medium=iphone\&share\_plat=ios\&share\_session\_id=729BE3B9-FC06-4908-B3A8-B2A4C6A2F211\&share\_source=COPY\&share\_tag=s\_i\&spmid=playlist.playlist-video-detail.0.0\&timestamp=1714734626\&unique\_k=vNkIORL\&up\_id=233956865](https://www.bilibili.com/video/BV1yU4y1f73i/?buvid=Y8470B823E0F865B46FD815AF771E428155B&from_spmid=main.space-contribution.0.0&is_story_h5=false&mid=e%2FMUnAJwgZE4We6tzMXcpg%3D%3D&p=1&plat_id=315&share_from=ugc&share_medium=iphone&share_plat=ios&share_session_id=729BE3B9-FC06-4908-B3A8-B2A4C6A2F211&share_source=COPY&share_tag=s_i&spmid=playlist.playlist-video-detail.0.0&timestamp=1714734626&unique_k=vNkIORL&up_id=233956865 " Anki 自动发音模板 | MarginNote 制卡 | ios / android / pc 端通用_哔哩哔哩_bilibili 本模板采用自动 / 在线发音，卡组文件体积小、方便同步传输，ios / android / pc 端通用。两个模板选其一，导入 Anki 即可；MN 导出请使用【专用】文件夹里的模板；OS15 使用 tts 可能无法自动发音，建议使用 <audio> "通用" 模板；安卓端使用 tts 发音，部分机型可能需要搭配下载 " Google 文字转语音引擎" 来使用。可自行修改为美音 / 英, 视频播放 https://www.bilibili.com/video/BV1yU4y1f73i/?buvid=Y8470B823E0F865B46FD815AF771E428155B&from_spmid=main.space-contribution.0.0&is_story_h5=false&mid=e%2FMUnAJwgZE4We6tzMXcpg%3D%3D&p=1&plat_id=315&share_from=ugc&share_medium=iphone&share_plat=ios&share_session_id=729BE3B9-FC06-4908-B3A8-B2A4C6A2F211&share_source=COPY&share_tag=s_i&spmid=playlist.playlist-video-detail.0.0&timestamp=1714734626&unique_k=vNkIORL&up_id=233956865")

### 4.3 Creating Different Types of Anki Cards

- Word-selection card creation
  - Forum tutorial

    [【OhMyMN Tips & Tricks】Creating Anki vocabulary cards (word-selection card creation + original-sentence translation) - Anki Zone——Memory Palace - MarginNote Chinese Community 【MarginNote3 Creating Anki Cards | OhMyMN v4 Word-selection card creation + original-sentence translation ① | AutoComplete + AutoTranslate-Bilibili】 MarginNote3 Creating Anki Cards | OhMyMN v4 Word-selection card creation + original-sentence transl\&hellip; https://bbs.marginnote.com.cn/t/topic/34477](https://bbs.marginnote.com.cn/t/topic/34477 "【OhMyMN 使用技巧分享】制作Anki单词卡（划词制卡+原句翻译） - Anki专区——记忆宫殿 - MarginNote 中文社区 【MarginNote3制作Anki卡片| OhMyMN v4 划词制卡+原句翻译① | AutoComplete + AutoTranslate-哔哩哔哩】 MarginNote3制作Anki卡片 | OhMyMN v4 划词制卡+原句翻… https://bbs.marginnote.com.cn/t/topic/34477")
  - 【\[Beta] OhMyMN plugin v4.0.13 | MarginNote3 Word-selection card creation | AutoComplete+AutoTranslate | Anki template-Bilibili】 

    [\[Beta\] OhMyMN plugin v4.0.13 | MarginNote3 Word-selection card creation | AutoComplete+AutoTranslate | Anki template\_Bilibili\_bilibili -, Views 4641, Danmaku 0, Likes 75, Coins 56, Favorites 92, Shares 16, Video author 豆乳玉麒麟3分糖, Author bio per aspera ad astra., Related videos: Oh no, MarginNote 4 might be coming; OhMyMN plugin introduction and installation; MarginNote3 excerpt settings～ a beginner-friendly tutorial～; Fixing the Japanese/Korean text cloze issue | Anki template | All-in-one; iPad split-screen drag-and-drop | between apps https://www.bilibili.com/video/BV1bP4y1U7QD/?buvid=XU69945620C34231F92B351C4D695FA793D76\&from\_spmid=dt.space-dt.video.0\&is\_story\_h5=false\&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D\&p=1\&plat\_id=114\&share\_from=ugc\&share\_medium=android\&share\_plat=android\&share\_session\_id=aa2fb06c-9d37-4684-811e-86bd6aae2d65\&share\_source=COPY\&share\_tag=s\_i\&spmid=united.player-video-detail.0.0\&timestamp=1714733775\&unique\_k=xgLOctL\&up\_id=233956865](https://www.bilibili.com/video/BV1bP4y1U7QD/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=dt.space-dt.video.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=114&share_from=ugc&share_medium=android&share_plat=android&share_session_id=aa2fb06c-9d37-4684-811e-86bd6aae2d65&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733775&unique_k=xgLOctL&up_id=233956865 "[测试版] OhMyMN插件 v4.0.13 | MarginNote3 划词制卡 | AutoComplete+AutoTranslate | Anki模板_哔哩哔哩_bilibili -, 视频播放量 4641、弹幕量 0、点赞数 75、投硬币枚数 56、收藏人数 92、转发人数 16, 视频作者 豆乳玉麒麟3分糖, 作者简介 per aspera ad astra.，相关视频：不好，marginnote 4可能要出，ohMyMN插件 介绍及安装，MarginNote3 摘录设置～ 保姆级教程～，修改日韩文字遮挡问题 | Anki模板 | 三合一，iPad分屏拖拽 | app间 https://www.bilibili.com/video/BV1bP4y1U7QD/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=dt.space-dt.video.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=114&share_from=ugc&share_medium=android&share_plat=android&share_session_id=aa2fb06c-9d37-4684-811e-86bd6aae2d65&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733775&unique_k=xgLOctL&up_id=233956865")
- Phrase card creation

  【MarginNote3 Phrase card creation～ a beginner-friendly tutorial～ OhMyMN plugin～-Bilibili】

  [MarginNote3 Phrase card creation～ a beginner-friendly tutorial～ OhMyMN plugin～\_Bilibili\_bilibili 【OhMyMN】Download link<https://bbs.marginnote.cn/t/topic/20501【OhMyMN】User guide https://ohmymn.marginnote.cn/—————【Chinese first】—————AnotherAutoDef custom definition entry /(\\> \*\*\[a-z\]. *)/i excerpt keeps only the definition entry AutoReplace  custom (/\[a-z '-/\]+/g,"* \*\$\&am, Views 5 <https://www.bilibili.com/video/BV1B8411x7sB/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=dt.space-dt.video.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=2c842125-803b-4fee-9046-f886b146055f&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733725&unique_k=qfHtBdq&up_id=233956865>](https://www.bilibili.com/video/BV1B8411x7sB/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=dt.space-dt.video.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=2c842125-803b-4fee-9046-f886b146055f&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733725&unique_k=qfHtBdq&up_id=233956865 " MarginNote3 短语制卡～ 保姆级教程～ OhMyMN插件～_哔哩哔哩_bilibili 【OhMyMN】下载地址https://bbs.marginnote.cn/t/topic/20501【OhMyMN】使用指南https://ohmymn.marginnote.cn/—————【中文在前】—————AnotherAutoDef自定义定义联项/(\*\*[a-z].*)/i摘录仅保留定义项AutoReplace  自定义(/[a-z '-/]+/g,"**$&am, 视频播放量 5 https://www.bilibili.com/video/BV1B8411x7sB/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=dt.space-dt.video.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=2c842125-803b-4fee-9046-f886b146055f&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733725&unique_k=qfHtBdq&up_id=233956865")
- Multiple-choice card creation
  - 【Using the OhMyMN plugin | Creating multiple-choice questions | MarginNote3-Bilibili】

    [ OhMyMN v3.2.0 | Creating multiple-choice questions | Advanced template\_Bilibili\_bilibili OhMyMN v3.2.0 | Creating multiple-choice questions | Advanced template is episode 4 of the "Using the OhMyMN plugin | Creating multiple-choice questions | MarginNote3" series, which has 4 episodes in total. Favorite the video or follow the creator to stay up to date with more related videos. https://www.bilibili.com/video/BV1j341177WD/?buvid=XU69945620C34231F92B351C4D695FA793D76\&from\_spmid=main.space-contribution.0.0\&is\_story\_h5=false\&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D\&p=4\&plat\_id=116\&share\_from=ugc\&share\_medium=android\&share\_plat=android\&share\_session\_id=86e99c17-e085-4304-a1e6-ec8c564fcdac\&share\_source=COPY\&share\_tag=s\_i\&spmid=united.player-video-detail.0.0\&timestamp=1714733952\&unique\_k=fqfT6ob\&up\_id=233956865](https://www.bilibili.com/video/BV1j341177WD/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=main.space-contribution.0.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=4&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=86e99c17-e085-4304-a1e6-ec8c564fcdac&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733952&unique_k=fqfT6ob&up_id=233956865 " OhMyMN v3.2.0 | 制作选择题 | 进阶模板_哔哩哔哩_bilibili OhMyMN v3.2.0 | 制作选择题 | 进阶模板是使用OhMyMN插件 | 制作选择题 | MarginNote3的第4集视频，该合集共计4集，视频收藏或关注UP主，及时了解更多相关视频内容。 https://www.bilibili.com/video/BV1j341177WD/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=main.space-contribution.0.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=4&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=86e99c17-e085-4304-a1e6-ec8c564fcdac&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714733952&unique_k=fqfT6ob&up_id=233956865")
  - Forum tutorial

    [ 【OhMyMN Tips & Tricks】Regular expressions and the replace() function | Creating multiple-choice questions - Methods, Tips, Workflows - MarginNote Chinese Community 0⃣️ Introduction OhMyMN makes extensive use of "regular expressions and the replace() function" for custom operations.    For beginners, this is analogous to "Find and Replace" in Word.   Anki also uses "Find and Replace".   So\&hellip; https://bbs.marginnote.com.cn/t/topic/34960](https://bbs.marginnote.com.cn/t/topic/34960 " 【OhMyMN 使用技巧分享】正则表达式与replace() 函数 | 选择题制作 - 方法、技巧、工作流 - MarginNote 中文社区 0⃣️ 引言OhMyMN插件中，广泛运用了"正则表达式与 replace() 函数"，来进行自定义操作。    对于小白来说，这种操作可类比 Word 中的"查找替换"。   Anki 中，其实也会用到"查找替换"。   所… https://bbs.marginnote.com.cn/t/topic/34960")

### 4.4 How to Automatically Jump from Anki Back to MarginNote for Immersive Reading?

- Forum tutorial

  [ Anki auto-jump to MN, solving Anki template headaches, immersive learning 【split-screen + auto-jump + auto-play】 - Anki Zone——Memory Palace - MarginNote Chinese Community Using iPad split-screen—reviewing on the Anki side to track the review schedule while using MN as a scratch-card on the other—may be the simplest, easiest setup available right now 【Roughly what it looks like】         【How to set it up】 On Anki, add \<script type="text/javascript">  \&hellip; https://bbs.marginnote.com.cn/t/topic/22924](https://bbs.marginnote.com.cn/t/topic/22924 " Anki自动跳转MN，解决anki模板烦恼，沉浸式学习【分屏+自动跳转+自动播放】 - Anki专区——记忆宫殿 - MarginNote 中文社区 利用ipad分屏，一边用Anki记录复习周期，一边用MN做刮刮乐，可能是目前最简单易用的设置 【大致效果】         【如何设置】 anki上，加上 <script type="text/javascript">  … https://bbs.marginnote.com.cn/t/topic/22924")
- Bilibili tutorial

  [ Anki auto-jump to Eudic/MarginNote3 | Immersive vocabulary memorization | Auto-play cards/look up words\_Bilibili\_bilibili 【Jump to MarginNote】window.setTimeout(() => void document.querySelector("a").click(), 0.1)【Jump to Eudic】window.setTimeout(() => void document.getElementById("link").click(), 0.1)(you need to add scr before and after, Views 2490, Danmaku 1, Likes 50, https://www.bilibili.com/video/BV1rd4y1m7v6/?buvid=XU69945620C34231F92B351C4D695FA793D76\&from\_spmid=dt.space-search.video.0\&is\_story\_h5=false\&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D\&p=1\&plat\_id=116\&share\_from=ugc\&share\_medium=android\&share\_plat=android\&share\_session\_id=bbd72091-22f1-4636-9828-fe9f777dfc50\&share\_source=COPY\&share\_tag=s\_i\&spmid=united.player-video-detail.0.0\&timestamp=1714905977\&unique\_k=GBgBH4e\&up\_id=233956865\&share\_times=1](https://www.bilibili.com/video/BV1rd4y1m7v6/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=dt.space-search.video.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=bbd72091-22f1-4636-9828-fe9f777dfc50&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714905977&unique_k=GBgBH4e&up_id=233956865&share_times=1 " Anki自动跳转欧路词典/MarginNote3 | 沉浸式背词 | 自动播放卡片/查词_哔哩哔哩_bilibili 【跳转MarginNote】window.setTimeout(() => void document.querySelector("a").click(), 0.1)【跳转欧路词典】window.setTimeout(() => void document.getElementById("link").click(), 0.1)（前后要加scr, 视频播放量 2490、弹幕量 1、点赞数 50、 https://www.bilibili.com/video/BV1rd4y1m7v6/?buvid=XU69945620C34231F92B351C4D695FA793D76&from_spmid=dt.space-search.video.0&is_story_h5=false&mid=wlce3olFiKAiEU8eyvvy5Q%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=bbd72091-22f1-4636-9828-fe9f777dfc50&share_source=COPY&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1714905977&unique_k=GBgBH4e&up_id=233956865&share_times=1")
- Xiaohongshu tutorial

  [ Anki auto-jump to MarginNote | Immersive review🌟 - Xiaohongshu What it does: for a card exported from MarginNote to Anki, when reviewing in split-screen, the back of the Anki card shows the answer while also locating the card's position in MarginNote3. Setup tutorial: after importing the MN card into Anki, tap ⚙️ in Anki, tap Card Template, tap Back, and paste this code on the back (the number in the code can be changed; it represents the delay before jumping back to MN after the answer is shown)  Then return to the Anki home screen and go to Settings > Review > Auto-play cards  During each review 【split-screen + enable auto-play https://www.xiaohongshu.com/explore/641ed3720000000013000f84?app\_platform=ios\&app\_version=8.12.1\&share\_from\_user\_hidden=true\&type=normal\&author\_share=1\&xhsshare=CopyLink\&appuid=62de06bd000000001f017b4d\&apptime=1714906334](https://www.xiaohongshu.com/explore/641ed3720000000013000f84?app_platform=ios&app_version=8.12.1&share_from_user_hidden=true&type=normal&author_share=1&xhsshare=CopyLink&appuid=62de06bd000000001f017b4d&apptime=1714906334 " Anki自动跳转MarginNote|沉浸式复习🌟 - 小红书 实现效果:从MarginNote导出到Anki的卡片，在分屏进行复习时，Anki背面显示答案的同时定位到其在MarginNote3中的卡片位置。 设置教程: 在MN的卡片导入Anki后，点击Anki中的⚙️，点击卡片模板 点击背面，在背面粘贴该代码 (代码中的数字可以更改，代表显示答案后延时跳转回MN的时间)  然后回到anki首页，进入设置>复习>自动播放卡片  在每次复习时【分屏+打开自动播放 https://www.xiaohongshu.com/explore/641ed3720000000013000f84?app_platform=ios&app_version=8.12.1&share_from_user_hidden=true&type=normal&author_share=1&xhsshare=CopyLink&appuid=62de06bd000000001f017b4d&apptime=1714906334")

## 5 Pre-Export Checklist

We recommend confirming each item:

1. The front and back of your key cards are set up;
2. The cloze types you need are working as expected;
3. If using a custom template, the apkg file is ready;
4. If you need MN backlinks / child-link images / voice, you have first checked the corresponding export options in the default template.

## 6 How to Give an Exported Card Deck a Hierarchical Structure?

### 6.1 Card Deck Naming Rules

Use two consecutive colons "::" to divide a card deck's hierarchical structure

### 6.2 Exporting a Card Deck with a Hierarchical Structure

#### 6.2.1 Export Result for a Card Deck with Ordinary Naming

![Export result for an ordinary card deck Export result for an ordinary card deck ](image/1495474c07358e85.webp)

#### 6.2.2 Export Result After Naming a Card Deck by Hierarchy

![Export result for a card deck with a hierarchical structure Export result for a card deck with a hierarchical structure ](image/ec04827a1cae1900.webp)

## 7 More Anki-Related Content

### 7.1 Exporting to Anki via Shortcuts

- 1. Install the "Export to Anki" shortcut

  [Shortcuts  https://www.icloud.com/shortcuts/b6c5ae3f0a5241019f918a121b318824](https://www.icloud.com/shortcuts/b6c5ae3f0a5241019f918a121b318824 "Shortcuts  https://www.icloud.com/shortcuts/b6c5ae3f0a5241019f918a121b318824")
- 2. Adjust the shortcut as needed, following AnkiMobile's URL scheme
  - AnkiMobile's URL scheme
    - The fixed prefix for adding a note:
      > anki://x-callback-url/addnote?
    - You can choose from the following parameters as needed:
      | Parameter | Meaning |
      | --------- | -------- |
      | profile   | Username |
      | type      | Note template name |
      | deck      | Deck name |
      | fld       | Field input prefix |
      | tags      | Tags |
      | dupes=1   | Allow adding duplicate notes |
      | x-success | Return after the note is added |
    - For more detailed parameters, see:

      [URL Schemes - AnkiMobile Manual  https://docs.ankimobile.net/url-schemes.html](https://docs.ankimobile.net/url-schemes.html "URL Schemes - AnkiMobile Manual  https://docs.ankimobile.net/url-schemes.html")
  - Adjust the shortcut

    Modify or add the note template name, deck name, field names, tags, and so on.

    ![Modifying shortcut parameters Modifying shortcut parameters ](image/236ef3b8d6b73da2.webp)
- 3. Run the "Export to Anki" shortcut
  - Select a card → open the "Card Editor" → … (More) → run the "Export to Anki" shortcut;
  - Select the question first, then the answer; you can select multiple;
  - Tap "Done" to export to Anki.
    ![Running the "Export to Anki" shortcut Running the "Export to Anki" shortcut ](image/c2869f7687894a42.webp)

### 7.2 Anki User Manuals

- Anki Manual (desktop)

  [ Introduction - Anki Manual  https://docs.ankiweb.net](https://docs.ankiweb.net " Introduction - Anki Manual  https://docs.ankiweb.net")
- AnkiMobile Manual (iOS/iPadOS)

  [ Intro - AnkiMobile Manual  https://docs.ankimobile.net](https://docs.ankimobile.net " Intro - AnkiMobile Manual  https://docs.ankimobile.net")

### 7.3 Common Anki Add-ons

- Add-on download site

  [   https://ankiweb.net/shared/addons](https://ankiweb.net/shared/addons "   https://ankiweb.net/shared/addons")
- Common add-on codes
  - Review Heatmap, a review visualization add-on (code: 1771074083)

    [   https://ankiweb.net/shared/info/1771074083](https://ankiweb.net/shared/info/1771074083 "   https://ankiweb.net/shared/info/1771074083")
  - Edit Field During Review, an add-on for editing during review (code: 1020366288)

    [   https://ankiweb.net/shared/info/1020366288](https://ankiweb.net/shared/info/1020366288 "   https://ankiweb.net/shared/info/1020366288")
  - Customize Keyboard Shortcuts, a keyboard-shortcut customization add-on (code: 24411424)

    [   https://ankiweb.net/shared/info/24411424](https://ankiweb.net/shared/info/24411424 "   https://ankiweb.net/shared/info/24411424")
  - Image Occlusion Enhanced, an image cloze add-on (code: 1374772155)

    [   https://ankiweb.net/shared/info/1374772155](https://ankiweb.net/shared/info/1374772155 "   https://ankiweb.net/shared/info/1374772155")
  - AnkiConnect add-on (code: 2055492159)

    [   https://ankiweb.net/shared/info/2055492159](https://ankiweb.net/shared/info/2055492159 "   https://ankiweb.net/shared/info/2055492159")
  - Batch Editing, a batch-editing add-on (code: 291119185)

    [   https://ankiweb.net/shared/info/291119185](https://ankiweb.net/shared/info/291119185 "   https://ankiweb.net/shared/info/291119185")
