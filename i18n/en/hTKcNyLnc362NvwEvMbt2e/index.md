# Third-Party App Integration ②: Obsidian+MN4

***

> 💡 Using the Obsidian-Bridge plugin (on the MarginNote side) together with the MarginNote Companion plugin (on Obsidian), you can **transfer notes between MarginNote and Obsidian**. You can create notes in MarginNote and then easily sync them to Obsidian, where you can use bidirectional links and the graph view to deepen your understanding and connect knowledge, building a unified, interconnected, and ever-growing personal knowledge base.
> 
> [ 【Third-Party MN Plugin】Obsidian-Bridge (Dynamic Markdown Export) — Connecting Two Knowledge Worlds #Ver.3.0.0 Officially Signed# - #162, by Deanlzy - Plugin Release Area｜Unrestricted editing and updating of the main post is allowed - MarginNote Chinese Community Obsidian BridgeThe Obsidian Bridge plugin builds a bridge from MarginNote to Obsidian. Through it, we can import the writing material / creative inspiration accumulated in MarginNote into Obsidian, using Ma\&hellip; https://bbs.marginnote.com.cn/t/topic/21235/162](https://bbs.marginnote.com.cn/t/topic/21235/162 " 【第三方MN插件】Obsidian-Bridge（Markdown动态导出）——连接两个知识星球 #Ver.3.0.0 已获官方签名# - #162，来自 Deanlzy - 插件发布区｜允许不受限制地编辑更新主帖 - MarginNote 中文社区 Obsidian BridgeObsidian Bridge 插件架起了 MarginNote 通往 Obsidian 的桥梁，通过它，我们可以把在 MarginNote 中积累的写作素材/创作灵感导入到 Obsidian 中，使用 Ma… https://bbs.marginnote.com.cn/t/topic/21235/162")

## 1 Plugin Installation and Configuration

### 1.1 Installing the MarginNote Plugin: Obsidian-Bridge

- Plugin download link:

  [  https://bbs.marginnote.com.cn/uploads/short-url/8IJ9ATwDfjc1gin61T3n0MGcDsa.mnaddon](https://bbs.marginnote.com.cn/uploads/short-url/8IJ9ATwDfjc1gin61T3n0MGcDsa.mnaddon "  https://bbs.marginnote.com.cn/uploads/short-url/8IJ9ATwDfjc1gin61T3n0MGcDsa.mnaddon")
- Installation method: How to install a plugin?
- Plugin configuration: No configuration is needed after the plugin is installed.

### 1.2 Installing the Obsidian Plugin: MarginNote Companion

-  Plugin download link:
  - For MarginNote3

    [  https://github.com/aidenlx/marginnote-companion](https://github.com/aidenlx/marginnote-companion "  https://github.com/aidenlx/marginnote-companion")
  - For MarginNote4

    [   https://github.com/pazerW/marginnote-companion/releases](https://github.com/pazerW/marginnote-companion/releases "   https://github.com/pazerW/marginnote-companion/releases")
- Installation method:
  1. Open Obsidian settings
  2. Click `Third-party plugins`
  3. Turn off `Safe mode`
  4. Open the `plugins folder`
  5. Unzip the downloaded plugin, then move the resulting folder into the plugins folder you opened
     ![Obsidian plugin installation interface Obsidian plugin installation interface ](image/2e1229d24a9a4e54.webp)
- Plugin configuration: After the plugin is installed, you can use the default template, or configure it yourself as needed by following the MarginNote Companion plugin manual.

  [Templates · aidenlx/marginnote-companion Wiki · GitHub An Obsidian plugin to bridge MarginNote 3 and Obsidian.md - Templates · aidenlx/marginnote-companion Wiki https://github.com/aidenlx/marginnote-companion/wiki/Templates](https://github.com/aidenlx/marginnote-companion/wiki/Templates "Templates · aidenlx/marginnote-companion Wiki · GitHub An Obsidian plugin to bridge MarginNote 3 and Obsidian.md - Templates · aidenlx/marginnote-companion Wiki https://github.com/aidenlx/marginnote-companion/wiki/Templates")

## 2 Using the Plugin

> 💡 The plugin supports two data import methods: basic excerpt import and Table of Contents tree import.

### 2.1 Basic Excerpt Import

> 💡 A single import supports either one card or a hand tool selection.
> 
> - Single card: supports text and images, but not handwriting inside the card.
> - Selection: supports text but not images; a rectangular selection is automatically OCR'd.

1. Open MarginNote4, enter a study set, then tap the plugin icon to launch the Obsidian-Bridge plugin.

   ![MarginNote4 interface MarginNote4 interface ](image/d57339e10a6f7f64.webp)
2. Now, whether you tap a card or use the hand tool to box-select content, the plugin will copy the note's information.
3. Import the note data in Obsidian
   - **Auto-paste**: Press the auto-paste toggle (default shortcut ⌘+R; you can also configure it yourself on Obsidian's hotkey settings page). Once auto-paste mode is on, you only need to keep Obsidian running in the background, and any content you tap or box-select in MarginNote will be automatically imported into Obsidian.

> 💡 We recommend using auto-paste mode.

### 2.2 Table of Contents Tree Import (TOC Mode)

> 💡 Best used when you want to quickly move an entire book's structure into Obsidian. It supports text only; images and handwriting inside cards cannot be imported.

1. Open MarginNote4, enter a study set, then tap the plugin icon to launch the Obsidian-Bridge plugin. Once it is running, tap the plugin again to open its mode settings.

   ![Obsidian-Bridge plugin settings page Obsidian-Bridge plugin settings page ](image/97b18e7149bdf2c0.webp)
2. Tap `✅Enable TOC capture mode`
3. Tap the top-level card of the mind map section you want to import.

   ![Usage example Usage example ](image/0ef83d56470ba4bc.webp)
4. Import the note data in Obsidian
   - **Manual paste:**   In Obsidian, press the paste key (⌘+V).
   - **Command paste:** Use OB's command palette and press ⌘+P (Obsidian's default command palette shortcut). Find the MarginNote Companion plugin command and choose `Insert TOC (default template) into current note`.

     ![Obsidian command palette Obsidian command palette ](image/ec1c1922b201529d.webp)
   - **Auto-paste**: Press the auto-paste toggle (default shortcut ⌘+R; you can also configure it yourself on Obsidian's hotkey settings page). Once auto-paste mode is on, you only need Obsidian in the background, and any content you tap or box-select in MarginNote will be automatically imported into Obsidian.

## 3 Showcase

> 💡 The showcase below is based on a custom template. Compared with the default template, it uses Callouts to beautify the styling and improve the hierarchy display. Learners are welcome to share their own custom templates on the forum.
> 
> [MarginNote Chinese Community - Multiply efficiency, share experience, spread the spirit of book lovers Reading & note-taking software MarginNote — product user feedback community   京ICP备17035497号-1 https://bbs.marginnote.com.cn/](https://bbs.marginnote.com.cn/ "MarginNote 中文社区 - 倍化效率，分享经验，传播爱书者的精神 阅读笔记软件MarginNote——产品用户反馈社区   京ICP备17035497号-1 https://bbs.marginnote.com.cn/")

### 3.1 Selected Text

```markdown 
> [!QUOTE] Excerpt
> {{Selection}}
> 🔖《{{DocTitle}}》

```


![](image/00ea4c1e80915546.webp)

![](image/70f0ae05652068cf.webp)

### 3.2 Note

```markdown title="Note body"
# {{#Title}}{{Title}}{{/Title}}{{^Title}}Untitled{{/Title}} {{Link}}
> [!NOTE]
{{#Excerpt}}> {{Excerpt}}
{{/Excerpt}}{{> Comments}}
```


```markdown title="Comment"
{{#Text}}>
> {{Text}} {{Link}}{{/Text}}
```


```markdown title="Merged note"
>
> {{Excerpt}} {{Link}}
```


![MarginNote card MarginNote card ](image/f51fdcf6285b8e58.webp)

![Result of importing a card into Obsidian Result of importing a card into Obsidian ](image/28509f7f223260eb.webp)

### 3.3 Table of Contents

```markdown 
# {{#Summary.Title}}{{Summary.Title}}{{/Summary.Title}}{{^Summary.Title}}Original text{{/Summary.Title}} 
{{#Summary.Excerpt}}> [!NOTE] {{Link}}
> {{Summary.Excerpt}}{{#Summary.Comments}}
>
> 📝 **Comment**：{{Summary.Comments}}{{/Summary.Comments}}{{/Summary.Excerpt}}{{^Summary.Excerpt}}{{#Summary.Comments}}> [!NOTE] {{Link}}
> 📝 **Comment**：{{Summary.Comments}}{{/Summary.Comments}}{{/Summary.Excerpt}}
```


![Obsidian plugin TOC settings Obsidian plugin TOC settings ](image/5c608c9591d6f606.webp)

![MarginNote card MarginNote card ](image/59a57327dbbeb2f0.webp)

![Result of importing a TOC into Obsidian Result of importing a TOC into Obsidian ](image/3d2929de766ae04a.webp)
