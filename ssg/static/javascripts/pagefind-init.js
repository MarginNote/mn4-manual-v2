/* Pagefind 搜索初始化（CJK 友好的静态站搜索）。
 *
 * 复用 Material 的 #__search 复选框开关 + extra.css 的纯 CSS 模态显隐——
 * 不引入任何 SPA / 路由 / 自定义模态逻辑。/pagefind/pagefind-ui.js 由构建后的
 * `pagefind` 步骤生成，并经 extra_javascript 先于本文件加载。
 */
(function () {
  function focusInput() {
    var input = document.querySelector("#pagefind .pagefind-ui__search-input");
    if (input) input.focus();
  }

  function init() {
    if (window.PagefindUI && document.getElementById("pagefind")) {
      new window.PagefindUI({
        element: "#pagefind",
        showSubResults: true,
        showImages: false,
        excerptLength: 18,
        autofocus: false,
        translations: {
          placeholder: "搜索手册…",
          zero_results: "未找到「[SEARCH_TERM]」相关内容",
        },
      });
    }

    var toggle = document.getElementById("__search");
    if (!toggle) return;

    // 打开模态时聚焦输入框
    toggle.addEventListener("change", function () {
      if (toggle.checked) setTimeout(focusInput, 40);
    });

    // "/" 打开，Esc 关闭
    document.addEventListener("keydown", function (e) {
      var t = e.target || {};
      var tag = (t.tagName || "").toLowerCase();
      var typing = tag === "input" || tag === "textarea" || t.isContentEditable;
      if (e.key === "/" && !typing && !toggle.checked) {
        e.preventDefault();
        toggle.checked = true;
        setTimeout(focusInput, 40);
      } else if (e.key === "Escape" && toggle.checked) {
        toggle.checked = false;
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
