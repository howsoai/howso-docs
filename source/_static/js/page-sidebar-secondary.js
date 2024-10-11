"use strict";

document.addEventListener("DOMContentLoaded", () => {
  const sidebarSecondaryItems = document.querySelector(
    ".sidebar-secondary-items"
  );
  if (!sidebarSecondaryItems) {
    return;
  }

  // Format Table Of Contents
  (() => {
    const tableOfContents = sidebarSecondaryItems.querySelector("nav.page-toc");
    if (!tableOfContents) {
      return;
    }

    // Truncate table of content's that have '.' notations to their final entry
    const internalLinks =
      tableOfContents.querySelectorAll(".internal.nav-link");
    internalLinks.forEach((link) => {
      const pre = link.querySelector(".pre");
      if (
        !pre ||
        !pre.textContent ||
        // Avoid adjusting any items that are language like
        !pre.textContent.match(/^[\w\d-.\(\)]*$/)
      ) {
        return;
      }
      const parts = pre.textContent.split(".");
      if (parts.length > 1) {
        pre.innerHTML = "." + parts.pop();
      }
    });
  })();

  sidebarSecondaryItems.classList.add("opacity-100");
});
