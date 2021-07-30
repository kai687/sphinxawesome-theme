/*
 * Copy headerlinks to clipboard
 *
 */
import { Controller } from "stimulus"
import ClipboardJS from "clipboard"

export default class extends Controller {

  copyHeaderLink(event) {
    const hlClipboard = new ClipboardJS('.headerlink', {
      text: (trigger) => {
        return trigger.href
      }
    })
    event.preventDefault()

    hlClipboard.on("success", this.showTooltip)
  }

  showTooltip(event) {
    const btn = event.trigger
    const before = btn.getAttribute("aria-label")
    btn.setAttribute("aria-label", "Copied!")
    setTimeout(() => {
      btn.setAttribute("aria-label", before)
    }, 2500)
  }
}
