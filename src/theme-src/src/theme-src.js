import "./theme-src.css";
import "./fonts.css";
import { navFunctions, collapsibleNav } from "./nav";
import { searchPane, clearSearchHighlights, searchEvents } from "./search";
import { showSnackbar } from "./snackbar";
import { showTooltip, hideTooltip, tooltipEvents } from "./tooltip";
import { scrollActive } from "./scroll";

// NOTE: strings should be encapsulated in _() which aliases
//       to Documentation.gettext() from Sphinx' doctools.js

navFunctions();
searchPane();
clearSearchHighlights();
searchEvents();
tooltipEvents();

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
    showTooltip(event);
  };
  btn.onfocus = (event) => {
    showTooltip(event);
  };

  btn.onmouseleave = hideTooltip;
  btn.onblur = hideTooltip;

  // Show 'Copied to clipboard' in a message at the bottom
  btn.onclick = () => {
    const selection = selectText(btn.parentNode);
    document.execCommand("copy");
    selection.removeAllRanges();
    showSnackbar(_("Copied code to clipboard"));
  };
});


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

collapsibleNav()
scrollActive();
