# Quick Sidebar Switching and Global Search

> 💡 The sidebar is a handy drawer for quickly swapping document files between study sets. It serves mainly as a file box, and when needed it lets you quickly switch to other projects and search global information, making it easy to cross-reference multiple materials.

![Left sidebar: quickly switch to other study sets/documents/mind maps, plus global search Left sidebar: quickly switch to other study sets/documents/mind maps, plus global search ](image/90b1f10c92fd8de8.webp)

## 1 Document Sidebar

Sidebar

In document view, tap the `Sidebar` button (shown by the icon above) to browse all items in your document library from the sidebar, achieving an effect similar to tab switching: switch between multiple documents to read and search.

![Click the target document in the sidebar to switch to that document view Click the target document in the sidebar to switch to that document view ](image/4c2b55575cb2dbc7.webp)

![(Animation) Bi-article comparison: press and hold the target document and drag it to the document area on the right to form a bi-article comparison view (Animation) Bi-article comparison: press and hold the target document and drag it to the document area on the right to form a bi-article comparison view ](image/24fa81f485e6bb3a.webp)

- **Switch documents**: Click the target document to switch to that document view
- **Bi-article comparison**: Press and hold the target document and drag it to the document area on the right to create a dual-document comparison view.
  > For more on bi-article comparison, see: [Comparison①: Bi-article Comparison Window](../n8VMVG5yoZj8WRatAPzJkm/index.md)
- **Change the document browsing scope**: Tap `All🔻`; by default documents are organized by `Category`. Tap the `<` to the left of `Category` to browse documents by `Folder`.
- **Import documents**: Tap `Import` and choose `From Files` or `From Web`
  > For more ways to import documents, see: [Importing Documents and Document Management](../ehTLoD9HictQhkFirV1g9k/index.md).
- **Search documents**: Tap 🔍 to search documents by **file name**

![Tap All🔻; by default documents are organized by Category Tap All🔻; by default documents are organized by Category ](image/250140648f752d94.webp)

![Tap the < to the left of Category to browse documents by Folder Tap the < to the left of Category to browse documents by Folder ](image/29538fa6a90527c7.webp)

![Tap Import and choose From Files or From Web Tap Import and choose From Files or From Web ](image/2befbed7ff8818d6.webp)

## 2 Study Set Sidebar

The study set sidebar displays all items in your study set library (including the documents and mind maps contained in each study set). It works much the same way as the document sidebar, but offers a richer set of features.

![Study set sidebar Study set sidebar ](image/db144a3787789124.webp)

- **Switch study sets**: Click the target study set/document/mind map/sub-mind map to switch to the corresponding view
- **Bi-article comparison**: Press and hold the target document and drag it to the document area on the right to form a bi-article comparison view; or tap the ellipsis to the right of the target document and choose `Open in Comparison View`
  > For more on bi-article comparison, see: [Comparison①: Bi-article Comparison Window](../n8VMVG5yoZj8WRatAPzJkm/index.md), [Comparison②: Cross-document Reference and Backlink](../2dQ7P1XFEV2UyqCLWyU7dU/index.md)
- **Import documents**: Tap `Import` and choose `From Files` or `From Web`
- **Global search**: Tap 🔍 to search documents by **name** or **full text**
  - `Name`: searches only document names, such as the names of PDFs or MP4s
  - `Full text`: searches the entire note and card database
  > 💡 The first time you use full-text search, it takes a few seconds to build the text index (depending on your total number of notes). Your device may warm up during this process, which is normal.
- **Open a sub-mind map in a floating view (card grouping board)**: Tap the ellipsis to the right of the target sub-mind map and choose `Open in Floating View` to browse that sub-mind map's cards in a floating card grouping board window (the `Card Source` is automatically set to that sub-mind map)
- **Browse a document's excerpt cards in the card grouping board**: Tap the ellipsis to the right of the target document and choose `Card Grouping Board` to browse that document's excerpt cards in a floating card grouping board window (the `Card Source` is automatically set to that document)

![The study set sidebar supports multiple viewing modes for mind maps and documents The study set sidebar supports multiple viewing modes for mind maps and documents ](image/1f68b51731ac7dd6.webp)

![Search by name or full text is supported Search by name or full text is supported ](image/231b648efc7a6138.webp)

![The result of opening the "Mistake Management" sub-mind map in a floating view The result of opening the "Mistake Management" sub-mind map in a floating view ](image/c8e1f98a36902df6.webp)

![Browsing the excerpt cards under the "Advanced Mathematics" document in the card grouping board Browsing the excerpt cards under the "Advanced Mathematics" document in the card grouping board ](image/2ffe58a4f5011673.webp)

## 3 Appendix: Full-text Search Supports Some Advanced Rules

The keywords AND, OR, NOT, and NEAR can be used to combine conditions and must be uppercase. (Lowercase versions are treated as ordinary search terms.)
Examples:
word1 AND word2 (contains word1 and word2)
word1 OR word2 (contains word1 or word2)
word1 NOT word2 (contains word1 but not word2)
word1 NEAR word2 (contains word1 and word2, with the two words close together)
word1 NEAR/2 word2 (contains word1 and word2, with the two words close together; the number indicates the proximity—the smaller it is, the closer they must be)
You can use parentheses to combine the above conditions into complex matching logic, for example:
word1 OR (word2 NOT word3)

A lowercase search term uses the beginswith matching mode.
An uppercase search term uses the fullmatch matching mode.

When searching document content, you can use file: to limit which files are searched, for example:
word1 file:Name2 (searches for the keyword word1 in the text content of PDFs whose directory/file name contains Name2.
