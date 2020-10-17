import { showSnackbar } from "./snackbar";
import ClipboardJS from "clipboard";

function copyEvents () {
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
