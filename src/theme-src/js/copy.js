import { showSnackbar } from "./snackbar";
import { showTooltip, hideTooltip } from "./tooltip";
import ClipboardJS from "clipboard";

function copyEvents () {
  //
  // Show and hide tooltips for the code copy buttons
  //
  document.querySelectorAll("button.copy").forEach((btn) => {
    ["mouseenter", "focus"].forEach((eventType) => {
      btn.addEventListener(eventType, (event) => {
        const tooltipText = event.target.getAttribute("aria-label");
        showTooltip(event, tooltipText);
      });
    });

    ["mouseleave", "blur"].forEach((eventType) => {
      btn.addEventListener(eventType, () => {
        hideTooltip();
      });
    });
  });
  //
  // Show and hide tooltips for the headerlink links
  //
  document.querySelectorAll(".headerlink").forEach((btn) => {
    ["mouseenter", "focus"].forEach((eventType) => {
      btn.addEventListener(eventType, (event) => {
        const tooltipText = event.target.getAttribute("aria-label");
        showTooltip(event, tooltipText);
      });
    });

    ["mouseleave", "blur"].forEach((eventType) => {
      btn.addEventListener(eventType, () => {
        hideTooltip();
      });
    });
    // we don't want the default `link` focus when clicked
    btn.onclick = (event) => {
      event.preventDefault();
    };
  });

  // Use clipboard.js for the headerlinks. Copy the href.
  const headerlinkClipboard = new ClipboardJS(".headerlink", {
    text: (trigger) => {
      return trigger.href;
    },
  });

  headerlinkClipboard.on("success", () => {
    showSnackbar(_("Copied link to clipboard!"));
  });

  // Use clipboard.js for the code copy buttons. Select the parent node.
  const codeClipboard = new ClipboardJS("button.copy", {
    target: (trigger) => {
      return trigger.parentNode;
    },
  });

  codeClipboard.on("success", () => {
    showSnackbar(_("Copied code to clipboard!"));
  });
}

export { copyEvents }
