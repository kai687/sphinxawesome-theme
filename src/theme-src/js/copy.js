import ClipboardJS from "clipboard";

function showSuccessTooltip (event) {
  // change the tooltip message on successful copy event
  const btn = event.trigger;
  const before = btn.getAttribute("aria-label");
  btn.setAttribute("aria-label", "Copied!");
  setTimeout(() => {
    btn.setAttribute("aria-label", before);
  }, 2500);
}

function copyEvents () {
  // Use clipboard.js for the headerlinks. Copy the href.
  const headerlinkClipboard = new ClipboardJS(".headerlink", {
    text: (trigger) => {
      return trigger.href;
    },
  });

  headerlinkClipboard.on("success", showSuccessTooltip);

  // we don't want the default event, since we're using it like a button
  document.querySelectorAll(".headerlink").forEach((link) => {
    link.onclick = (event) => {
      event.preventDefault();
    }
  });

  // Use clipboard.js for the code copy buttons. Select the parent node.
  const codeClipboard = new ClipboardJS("button.copy", {
    target: (trigger) => {
      return trigger.parentNode;
    },
  });

  codeClipboard.on("success", showSuccessTooltip);
}

export { copyEvents }
