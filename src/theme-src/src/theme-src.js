import "./theme-src.css";
import "./fonts.css";

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
    nav.setAttribute("data-menu", "open");
  });
}

const closeNavBtn = document.querySelector("#closeNavBtn");
if (closeNavBtn) {
  closeNavBtn.addEventListener("click", () => {
    nav.setAttribute("data-menu", "closed");
  });
}

// We want to close the nav menu also, when clicking on a link in the nav menu on the
// current page (but only on small screens (i.e., where the close button is visible))
document.querySelectorAll("nav li.current a").forEach((link) => {
  if (closeNavBtn.offsetWidth > 0 && closeNavBtn.offsetHeight > 0) {
    link.addEventListener("click", () => {
      nav.setAttribute("data-menu", "closed");
    });
  }
});

const openSearchBtn = document.querySelector("#openSearchBtn");
if (openSearchBtn) {
  openSearchBtn.addEventListener("click", () => {
    search.setAttribute("data-menu", "open");
  });
}

const closeSearchBtn = document.querySelector("#closeSearchBtn");
if (closeSearchBtn) {
  closeSearchBtn.addEventListener("click", () => {
    search.setAttribute("data-menu", "closed");
  });
}

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
    tooltip.textContent = _("Copy this code");
  });

  btn.addEventListener("mouseleave", () => {
    tooltip.textContent = "";
    tooltip.style.opacity = 0;
    tooltip.style.visibility = "hidden";
  });

  // Show 'Copied to clipboard' in a message at the bottom
  btn.addEventListener("click", () => {
    const selection = selectText(el);
    document.execCommand("copy");
    selection.removeAllRanges();
    showSnackbar(_("Copied code to clipboard"));
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

// Add Copy Button to all code blocks
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
      _("Clear highlighted words") +
      "</a>";
    snackbar.classList.remove("bg-gray-900", "text-gray-100");
    snackbar.classList.add("bg-gray-200", "text-blue-600");
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

function showSnackbar(message) {
  snackbar.textContent = message;
  snackbar.style.opacity = 1;
  snackbar.style.transform = "translate(0,0)";
  setTimeout(hideSnackbar, 2000);
}

function hideSnackbar() {
  snackbar.style.opacity = 0;
  snackbar.style.transform = "translate(0,100%)";
  snackbar.classList.remove("bg-gray-200", "text-blue-600");
  snackbar.classList.add("bg-gray-900", "text-gray-100");
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
});

// click on permalink copies the href to clipboard
document.querySelectorAll(".headerlink").forEach((link) => {
  link.addEventListener("click", (event) => {
    copyToClipboard(link.href, _("Copied link to clipboard"));
    event.preventDefault();
  });
});

function copyToClipboard(str, msg) {
  const el = document.createElement("textarea");
  el.value = str;
  el.setAttribute("readonly", "");
  el.style.position = "absolute";
  el.style.left = "-9999px";
  document.body.appendChild(el);
  const selected =
    document.getSelection().rangeCount > 0
      ? document.getSelection().getRangeAt(0)
      : false;
  el.select();
  document.execCommand("copy");
  document.body.removeChild(el);
  if (selected) {
    document.getSelection().removeAllRanges();
    document.getSelection().addRange(selected);
  }
  showSnackbar(msg);
}
