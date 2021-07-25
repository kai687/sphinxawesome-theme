// Open/close the sidebar
import { Controller } from "stimulus"

export default class extends Controller {

  static targets = ["sidebar", "screen"]

  initialize() {
    this.page = this.element
  }

  open() {
    this.page.classList.add("isShown")
    this.sidebarTarget.classList.add("isShown")
    this.screenTarget.classList.add("isShown")
  }

  close() {
    this.page.classList.remove("isShown")
    this.sidebarTarget.classList.remove("isShown")
    this.screenTarget.classList.remove("isShown")
  }

  // collapse/expand navigation sections
  expand(event) {
    const icon = event.currentTarget
    icon.parentElement.parentElement.classList.toggle("expanded")
  }
}
