/*
 * Copy code blocks to clipboard
 */
import { Controller } from "@hotwired/stimulus";
import Clipboard from "clipboard";

export default class extends Controller {
  static targets = ["button"];

  connect() {
    const pre = this.element.querySelector("pre");
    this.pre = pre;
    this.label = "copy";

    if (pre) {
      const btn = document.createElement("button");
      btn.classList.add("copy");
      btn.setAttribute("data-code-target", "button");
      btn.setAttribute("data-action", "code#copy");
      btn.textContent = this.label;
      pre.appendChild(btn);
    }
  }

  copy() {
    const clipboard = new Clipboard(this.pre, {
      target: () => {
        return this.pre;
      },
    });

    clipboard.on("success", (e) => {
      if (this.hasButtonTarget) {
        this.buttonTarget.textContent = "copied!";
        setTimeout(() => (this.buttonTarget.textContent = this.label), 1500);
      }
    });

    clipboard.on("error", (e) => {
      console.error(e.action);
      console.error(e.trigger);
    });
  }
}
