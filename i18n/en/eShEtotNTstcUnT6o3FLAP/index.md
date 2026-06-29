# Markdown and Formulas

## 1 What Is Markdown

Markdown is a lightweight markup language designed for collaboration. Using simple, easy-to-understand syntax, it converts plain text into formatted HTML documents, helping learners format their text quickly as they write so they can focus better on the content itself;

With the help of various tools, Markdown documents can be easily converted into many file types such as TXT, PDF, Word, HTML, and ePub.

## 2 How to Enable Markdown Input in MarginNote?

In MarginNote 4, **while editing a text comment on a card**, learners can tap the `Markdown` option on the keyboard input bar to toggle Markdown mode for that comment. When you **add a new text comment** afterward, the Markdown mode on/off state carries over from the previous setting.

![Keyboard input bar in non-Markdown mode (Html mode) Keyboard input bar in non-Markdown mode (Html mode) ](image/52441f72ef7d38d4.webp)

![Keyboard input bar in Markdown mode Keyboard input bar in Markdown mode ](image/76d939f408b4f23a.webp)

> ⚠️Note: If you enable Markdown mode, the rich-text formatting (such as font and text size) edited in a text comment under Html mode will be lost. Even if you turn it off again immediately after enabling it, the original style settings will not be restored, so please be careful before enabling it.

## 3 Markdown Syntax Basics

### 3.1 Headings

There are two ways to write them:

![Markdown syntax for headings Markdown syntax for headings ](image/04adc36026577326.webp)

1. `#` + space + heading text

   Type a # at the beginning of the line, add a space, then type the heading text.
   ```markdown 
   # Heading 1
   ## Heading 2
   ### Heading 3
   #### Heading 4
   ##### Heading 5
   ###### Heading 6
   ```

   This syntax supports up to six heading levels, but in MarginNote 4 the size difference between level-5 and level-6 headings is minor.

1) Heading text + `===` / `---`
   ```markdown 
   Heading 1
   ===

   Heading 2
   ---
   ```

   This syntax supports only two heading levels.

### 3.2 Text Styles

![Basic Markdown text formatting Basic Markdown text formatting ](image/db6c5d7b87ae6c30.webp)

#### 3.2.1 Bold

**Bold text**

```markdown 
**Bold text**
```


#### 3.2.2 Italic

*Italic text*

```markdown 
_Italic text_

```


> 📌Nested usage of **bold** and *italic*
> 
> 1. ***Bold italic***
>    ```markdown 
>    __*Bold italic*__
>    ```
> 
> 2. **Emphasize with *****italic text***** inside bold text**
>    ```markdown 
>    **Emphasize with _italic text_ inside bold text**
>    ```
> 

#### 3.2.3 Strikethrough (Not yet supported in MN4)

~~Completed task~~

```markdown 
~~Completed task~~
```


#### 3.2.4 Footnotes (Not yet supported in MN4)

This is text that needs a note[^1]

(Due to differences in rendering, the footnote content for this page is displayed at the very bottom of this page.)

```markdown 
This is text that needs a note[^1]

[^1]: This is the explanatory content of a footnote.
```


> 💡If learners want to use Markdown to achieve additional text formatting effects such as underline, highlight, superscript and subscript, font size, font color, background color, and text alignment, please refer to the section on embedding HTML and CSS.

### 3.3 Paragraphs and Line Breaks

A paragraph in Markdown consists of one or more lines of text. In MarginNote 4, starting a new line marks a new paragraph; when using the keyboard, press `O``ption+Enter` to start a new line. In the current MN4 display, the spacing of a single line break and a blank line may look the same.

### 3.4 Lists

![Rendered result of lists Rendered result of lists ](image/e9ea29bc0c2be5c7.webp)

1. Ordered list: number + period + space + list content

   The first list number determines how the subsequent numbers are arranged.

   ![List numbering method List numbering method ](image/c47153f85626d0e1.webp)
2. Unordered list: "asterisk `*` / plus `+` / minus `-`" + space + list content

> 💡Tips: Ordered lists and unordered lists can be nested within each other.

### 3.5 Blockquotes

![Rendered result of blockquotes Rendered result of blockquotes ](image/be5f06e442dd4281.webp)

1. Blockquote marker: greater-than sign `>` + space.
   ```markdown 
   > Quote line one
   > 
   > Quote line two

   ```

2. Nested blockquotes
   ```markdown 
   > First-level quote
   > > Second-level quote
   ```

3. Quoting other elements
   ```markdown 
   > Quote **bold**
   > 1. Quote an ordered list
   > - Quote an unordered list

   ```

### 3.6 Horizontal Rules

![Rendered result of horizontal rules Rendered result of horizontal rules ](image/992fdeb745a3f0be.webp)

When learners want to create a dividing line between two paragraphs, the line in between must contain only three or more asterisks (`*`), underscores (`_`), or three space-separated minus signs (`-`).

```markdown 
Before the divider
- - -
***
___
After the divider
```


### 3.7 Code

![Rendered result of inline code Rendered result of inline code ](image/f0dd88624f94e7e6.webp)

1. Inline code: backtick (`` ` ``) + code content + backtick (`` ` ``)
   ```markdown 
   `Inline code`
   ```

2. Code block:
   1. Three backticks (`` ` ``) + line break + code content + line break + three backticks (`` ` ``)
      ```markdown 

      ```

      Code block 1
      ```text 

      ```

   2. Four spaces / `tab` + code content
      ```markdown 
          Code block 2
      ```

> 💡Tips: When learners want to type certain marker symbols in the Markdown editor but don't want those symbols to be rendered, they can use a backslash to escape them:
> 
> ```markdown 
> \!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~
> ```
> 

### 3.8 Hyperlinks

Links typed directly in the Markdown editor are converted into hyperlinks (wrapping a web address or email address in `<>` also converts it into a hyperlink). When multiple links look cluttered and unattractive, learners can use the following methods to make link expressions more elegant:

![Hyperlinks in Markdown Hyperlinks in Markdown ](image/3ce0ce94dfa4161c.webp)

1. Inline hyperlink: `[link text](link URL)`
   ```markdown 
   [MarginNote Forum](https://bbs.marginnote.com.cn)
   ```

2. Reference hyperlink (not yet supported in MN4): `[link text][link identifier]`, then define `[link identifier]: link URL` in another paragraph
   ```markdown 
   This link uses 1 as the URL variable [MarginNote Forum][1]
   Then assign a value (URL) to the variable at the end of the document

     [1]: https://bbs.marginnote.com.cn
   ```

Hyperlinks now support card URLs; for details, see [Card Links ⑤ | Inline Links](../sncaMzMHTBx6abg1dZcPfB/index.md).

### 3.9 Images (Not yet supported in MN4)

```markdown 
![alt text for the image](image URL)

```


### 3.10 Tables

![Rendered result of tables Rendered result of tables ](image/d5f725c0a80a6d95.webp)

1. Table
   ```markdown 
   Header cell 1 | Header cell 2
   --------- | -------------
   Content cell, column 1 row 1 | Content cell, column 2 row 1
   Content cell, column 1 row 2, with extra text | Content cell, column 2 row 2
   ```

2. Table alignment
   ```markdown 
   | Left-aligned | Right-aligned | Center-aligned |
   | :-----| ----: | :----: |
   | Cell | Cell | Cell |
   | Cell | Cell | Cell |
   ```

## 4 Advanced Markdown Syntax

### 4.1 Formulas

The Markdown editor in MarginNote 4 supports entering formulas using LaTeX, KaTeX, MathJax, and HTML tags. Learners who want to know how to edit formulas with Markdown can learn the syntax for Markdown formulas through the [Help Documentation](https://www.latexlive.com/help "Help Documentation"), or directly generate the Markdown code for a formula using the [web editor tool](https://www.latexlive.com/home "web editor tool").

### 4.2 Embedded HTML and CSS

#### 4.2.1 Underline

![  ](image/835fc27b9b1a3c22.webp)

```markdown 
<u>Underline</u>

<span style="border-bottom:5px dashed green;">Underline 2</span>
```


#### 4.2.2 Highlight

![  ](image/e0eea1a8a2b04ef2.webp)

```markdown 
<mark>Highlighter</mark>
```


#### 4.2.3 Background Color

![  ](image/458aa6e0ec4b815a.webp)

```markdown 
<table><tr><td bgcolor=yellow>Background color yellow</td></tr></table>
```


#### 4.2.4 Text Alignment

![  ](image/4b986084efe18f0a.webp)

```markdown 
<center>Center</center>
<p align="left">Left-aligned</p>
<p align="right">Right-aligned</p>
```


#### 4.2.5 Font Size

![  ](image/685c4866cac6c1a7.webp)

```markdown 
<small>Small font</small>
Normal font
<big>Large font</big>
```


#### 4.2.6 Text Color

![  ](image/5f6451bb5d48007c.webp)

```markdown 
<font color=red>Red</font>
<font color=#008000>Green</font>
```


Tips: Combined use of text and color

![  ](image/8030737ed073ab34.webp)

```markdown 
<font size=5 color=red>Red text with size=5</font>
```


#### 4.2.7 Superscript and Subscript

![  ](image/2ed671522362b490.webp)

```markdown 
This is <sup>superscript</sup> text
```


![  ](image/7efe1db65cc90307.webp)

```markdown 
This is <sub>subscript</sub> text
```


Images and tables can also be further beautified with HTML and CSS. For more tutorials on beautifying with HTML and CSS, refer to [w3scnool](https://www.w3school.com.cn/index.html "w3scnool") and [RUNOOB Tutorial](https://www.runoob.com/html/html-tutorial.html "RUNOOB Tutorial").

### 4.3 Forum Plugin Extensions

Plugins created by users on the [MarginNote Forum](https://bbs.marginnote.com.cn "MarginNote Forum") provide many features not yet supported in MarginNote 4's Markdown. For example, learners who need more advanced Markdown functionality can also use the [Milkdown plugin](https://bbs.marginnote.com.cn/t/topic/34772 "Milkdown plugin"). If you want to quickly create diagrams within a card, you can also use the [Excalidraw plugin](https://bbs.marginnote.com.cn/t/topic/46056 "Excalidraw plugin"), as well as plugins like [CKEditor](https://bbs.marginnote.com.cn/t/topic/7282 "CKEditor") and [myMarkDown](https://bbs.marginnote.com.cn/t/topic/13635 "myMarkDown") to help beautify cards.

[^1]: This is the explanatory content of a footnote.
