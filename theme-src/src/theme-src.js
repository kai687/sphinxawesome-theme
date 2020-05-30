import "./theme-src.css";
import "./fonts.css";

// NOTE: strings should be encapsulated in _() which aliases
//       to Documentation.gettext() from Sphinx' doctools.js

// NOTE: strings should be encapsulated in _() which aliases
//       to Documentation.gettext() from Sphinx' doctools.js

// DOM elements we want to manipulate
const nav = document.querySelector("nav");
const search = document.querySelector("#search-pane");
const tooltip = document.querySelector("#tooltip");
const snackbar = document.querySelector("#snackbar");
const searchForm = document.querySelector("#searchbox");
const searchInput = document.querySelector("#search-input");

const openNavBtn = document.querySelector("#openNavBtn");
if (openNavBtn) {
  openNavBtn.addEventListener("click", () => {
    nav.style.transform = "translate(0,0)";
    nav.style.transition = "transform 0.3s, opacity 0.5s";
    nav.style.opacity = 1;
  });
}

const closeNavBtn = document.querySelector("#closeNavBtn");
if (closeNavBtn) {
  closeNavBtn.addEventListener("click", () => {
    nav.style.transform = "translate(-100%, 0)";
    nav.style.opacity = 0;
  });
}

document.querySelector("#openSearchBtn").addEventListener("click", () => {
  search.style.transform = "translate(0,0)";
  search.style.transition = "transform 0.3s, opacity 0.5s";
  search.style.opacity = 1;
});

document.querySelector("#closeSearchBtn").addEventListener("click", () => {
  search.style.transform = "translate(100%, 0)";
  search.style.opacity = 0;
});

function selectText(node) {
  const selection = window.getSelection();
  const range = document.createRange();
  range.selectNodeContents(node);
  selection.removeAllRanges();
  selection.addRange(range);

  return selection;
}

function addCopyButton(el) {
  const btn = document.createElement("button");
  btn.setAttribute("aria-label", _("Copy this code block"));
  btn.classList.add(
    "absolute",
    "right-0",
    "top-0",
    "p-2",
    "text-gray-600",
    "outline-none",
    "focus:outline-none",
    "focus:text-pink-500",
    "hover:text-pink-500"
  );
  btn.innerHTML =
    '<svg aria-hidden="true" class="h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M6 6V2c0-1.1.9-2 2-2h10a2 2 0 012 2v10a2 2 0 01-2 2h-4v4a2 2 0 01-2 2H2a2 2 0 01-2-2V8c0-1.1.9-2 2-2h4zm2 0h4a2 2 0 012 2v4h4V2H8v4zM2 8v10h10V8H2z"/></svg>';

  // Show a tooltip on hover
  btn.addEventListener("mouseenter", (event) => {
    const rect = event.target.getBoundingClientRect();
    tooltip.style.opacity = 0.6;
    tooltip.style.visibility = "visible";
    tooltip.style.top = rect.y + rect.height + 1 + "px";
    tooltip.style.left = rect.x - 4 + "px";
    tooltip.textContent = _("Copy");
  });

  btn.addEventListener("mouseleave", () => {
    tooltip.textContent = "";
    tooltip.style.opacity = 0;
    tooltip.style.visibility = "hidden";
  });

  // Show 'Copied to clipboard' in a message at the bottom
  btn.addEventListener("click", () => {
    snackbar.textContent = _("Copied to clipboard");
    snackbar.style.opacity = 1;
    snackbar.style.transform = "translate(0,0)";
    setTimeout(hideSnackbar, 2000);
    const selection = selectText(el);
    document.execCommand("copy");
    selection.removeAllRanges;
  });

  el.appendChild(btn);
}

// In order for 'literal blocks' to behave a little like the code blocks,
// we need to wrap them with a highlight div as well
document.querySelectorAll("pre.literal-block").forEach((block) => {
  const wrapper = document.createElement("div");
  wrapper.classList.add("highlight");
  block.parentNode.insertBefore(wrapper, block);
  wrapper.appendChild(block);
});

// Add Copy Button to all '<div class="highlight">'
document.querySelectorAll("div.highlight").forEach((code) => {
  code.style.position = "relative";
  addCopyButton(code);
});

// Display link to clear highlighting at the bottom
setTimeout(() => {
  const highlights = document.querySelectorAll(".highlighted");
  if (highlights.length) {
    snackbar.innerHTML =
      '<a class="tracking-wide" href="javascript:Documentation.hideSearchWords()">' +
      _("Clear Highlights") +
      "</a>";
    snackbar.style.opacity = 1;
    snackbar.style.transform = "translate(0,0)";

    document.querySelector("#snackbar > a").addEventListener("click", () => {
      hideSnackbar();
      searchInput.value = "";
    });

    // Add the currently searched for term in the input
    searchInput.value = highlights[0].textContent;
    searchInput.addEventListener("search", () => {
      Documentation.hideSearchWords();
      hideSnackbar();
    });
  }
}, 500);

// prevent empty search submit
searchForm.addEventListener("submit", (event) => {
  if (searchInput.value.length < 1) {
    event.preventDefault();
  }
});

function hideSnackbar() {
  snackbar.style.opacity = 0;
  snackbar.style.transform = "translate(0,100%)";
}

// focus search input on key '/'
window.addEventListener("keydown", (event) => {
  if (event.code === "Slash") {
    searchInput.focus();
    searchInput.value = "";
    event.preventDefault();
  }
  if (event.code === "Escape") {
    searchInput.blur();
    event.preventDefault();
  }
});

// hide 'copied' tooltip on scroll
window.addEventListener("scroll", () => {
  tooltip.textContent = "";
  tooltip.style.opacity = 0;
  tooltip.style.visibility = "hidden";
})
