// some enhancements about the search experience
import { Controller } from "stimulus"

export default class extends Controller {

  static targets = ["searchInput", "searchPane"]

  open() {
    console.log("Open it!!!")
    this.searchPaneTarget.classList.add("isShown")
  }

  close() {
    this.searchPaneTarget.classList.remove("isShown")
  }
}
