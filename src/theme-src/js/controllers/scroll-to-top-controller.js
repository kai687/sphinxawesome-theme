// Scroll to top button
import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = ["main", "scrollToTop"];

  scroll() {
    this.mainTarget.scrollTop = 0;
    window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
    this.scrollToTopTarget.blur();
  }

  showButton() {
    if (this.hasScrollToTopTarget) {
      if (this.mainTarget.scrollTop > 100 || window.scrollY > 100) {
        this.scrollToTopTarget.classList.add("isShown");
      } else {
        this.scrollToTopTarget.classList.remove("isShown");
      }
    }
  }
}
