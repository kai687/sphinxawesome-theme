// some enhancements about the search experience
import { Controller } from "stimulus";

export default class extends Controller {
  static targets = ["searchInput", "snackbar"];

  focus(event) {
    if (this.hasSearchInputTarget) {
      if (event.code === "Slash") {
        event.preventDefault();
        this.focusSearchInput();
      }

      if (event.code === "Escape") {
        event.preventDefault();
        this.blurSearchInput();
      }
    }
  }

  focusSearchInput() {
    this.searchInputTarget.focus();
  }

  blurSearchInput() {
    this.searchInputTarget.blur();
  }

  connect() {
    // check, if highlighting is active on this page
    const urlParams = new URLSearchParams(window.location.search);
    const highlighted = urlParams.get("highlight");
    if (highlighted) {
      this.showSnackbar();
      // set currently highlighted term in the search input
      this.searchInputTarget.value = highlighted;
    }
  }

  showSnackbar() {
    this.snackbarTarget.classList.add("isShown");
  }

  hideSnackbar() {
    Documentation.hideSearchWords();
    this.searchInputTarget.value = "";
    // remove the `?highlight=` from the URL
    const newURL = window.location.origin + window.location.pathname;
    window.history.pushState({}, document.title, newURL);
    this.snackbarTarget.classList.remove("isShown");
  }
}
