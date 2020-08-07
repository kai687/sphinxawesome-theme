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
  openNavBtn.onclick = () => {
    nav.setAttribute("data-menu", "open");
  };
}

const closeNavBtn = document.querySelector("#closeNavBtn");
if (closeNavBtn) {
  closeNavBtn.onclick = () => {
    nav.setAttribute("data-menu", "closed");
  };
}

// We want to close the nav menu also, when clicking on a link in the nav menu on the
// current page (but only on small screens (i.e., where the close button is visible))
document.querySelectorAll("nav li.current a").forEach((link) => {
  if (closeNavBtn.offsetWidth > 0 && closeNavBtn.offsetHeight > 0) {
    link.onclick = () => {
      nav.setAttribute("data-menu", "closed");
    };
  }
});

const openSearchBtn = document.querySelector("#openSearchBtn");
if (openSearchBtn) {
  openSearchBtn.onclick = () => {
    search.setAttribute("data-menu", "open");
  };
}

const closeSearchBtn = document.querySelector("#closeSearchBtn");
if (closeSearchBtn) {
  closeSearchBtn.onclick = () => {
    search.setAttribute("data-menu", "closed");
  };
}

function selectText(node) {
  const selection = window.getSelection();
  const range = document.createRange();
  range.selectNodeContents(node);
  selection.removeAllRanges();
  selection.addRange(range);

  return selection;
}

// Add behaviour to 'copy code' buttons
document.querySelectorAll("button.copy").forEach((btn) => {
  btn.onmouseenter = (event) => {
    const rect = event.target.getBoundingClientRect();
    tooltip.style.opacity = 0.6;
    tooltip.style.visibility = "visible";
    tooltip.style.top = rect.y + rect.height + 1 + "px";
    tooltip.style.left = rect.x - 4 + "px";
    tooltip.textContent = _("Copy this code");
  };

  btn.onmouseleave = () => {
    tooltip.textContent = "";
    tooltip.style.opacity = 0;
    tooltip.style.visibility = "hidden";
  };

  // Show 'Copied to clipboard' in a message at the bottom
  btn.onclick = () => {
    console.log(btn.parentNode);
    const selection = selectText(btn.parentNode);
    document.execCommand("copy");
    selection.removeAllRanges();
    showSnackbar(_("Copied code to clipboard"));
  };
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
    snackbar.classList.add("bg-gray-200", "text-blue-700");
    snackbar.style.opacity = 1;
    snackbar.style.transform = "translate(0,0)";

    document.querySelector("#snackbar > a").onclick = () => {
      hideSnackbar();
      searchInput.value = "";
    };

    // Add the currently searched for term in the input
    searchInput.value = highlights[0].textContent;
    searchInput.onsearch = () => {
      Documentation.hideSearchWords();
      hideSnackbar();
    };
  }
}, 500);

// prevent empty search submit
searchForm.onsubmit = (event) => {
  if (searchInput.value.length < 1) {
    event.preventDefault();
  }
};

function showSnackbar(message) {
  snackbar.textContent = message;
  snackbar.style.opacity = 1;
  snackbar.style.transform = "translate(0,0)";
  setTimeout(hideSnackbar, 2000);
}

function hideSnackbar() {
  snackbar.style.opacity = 0;
  snackbar.style.transform = "translate(0,100%)";
  snackbar.classList.remove("bg-gray-200", "text-blue-700");
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
window.onscroll = () => {
  tooltip.textContent = "";
  tooltip.style.opacity = 0;
  tooltip.style.visibility = "hidden";
};

// click on permalink copies the href to clipboard
document.querySelectorAll(".headerlink").forEach((link) => {
  link.onclick = (event) => {
    copyToClipboard(link.href, _("Copied link to clipboard"));
    event.preventDefault();
  };
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

// collapsible NAV
document.querySelectorAll(".expand").forEach((span) => {
  span.onclick = () => {
    span.parentElement.classList.toggle("expanded");
  };
});

// expand NAV when tab focus is received on link
document.querySelectorAll("#nav-toc a").forEach((navLink) => {
  if (navLink.nextElementSibling) {
    navLink.onfocus = () => {
      navLink.parentElement.classList.toggle("expanded");
    };
  }
});
