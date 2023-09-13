"use strict";
(function () {
  function onColorSchemeChange(query) {
    const icons = document.querySelectorAll("link[rel~='icon']");
    if (query.matches) {
      for (const link of icons) {
        link.href = link.href.replace("favicon.", "favicon-dark.");
      }
    } else {
      for (const link of icons) {
        link.href = link.href.replace("favicon-dark.", "favicon.");
      }
    }
  }
  const match = window.matchMedia("(prefers-color-scheme: dark)");
  match.addEventListener("change", onColorSchemeChange);
  onColorSchemeChange(match); // Initial State
})();
