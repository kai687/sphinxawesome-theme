// Scroll to top button
import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = ["main", "scrollToTop"];

  initialize() {
    this.lastPosition = 0;
    this.offset = 200;
  }

  scroll() {
    this.mainTarget.scrollTop = 0;
    window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
    this.scrollToTopTarget.blur();
  }

  showButton() {
    if (this.hasScrollToTopTarget) {
      const offsetCondition = this.mainTarget.scrollTop > this.offset;
      const scrollingUp = this.mainTarget.scrollTop < this.lastPosition;
      if (offsetCondition && scrollingUp) {
        this.scrollToTopTarget.classList.add("isShown");
      } else {
        this.scrollToTopTarget.classList.remove("isShown");
      }
    }
    this.lastPosition = this.mainTarget.scrollTop;
  }
}
