// Scroll to top button
import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = ["scrollToTop", "main"];

  connect() {
    this.lastPosition = 0;
    this.offset = 200;
  }

  scroll() {
    this.scrollWindow.scrollTop = 0;
    window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
    this.scrollToTopTarget.blur();
  }

  showButton() {
    if (this.hasScrollToTopTarget && this.hasMainTarget) {
      const offsetCondition =
        this.mainTarget.scrollTop > this.offset || window.scrollY > this.offset;

      if (this.mainTarget.scrollTop > 0 && window.scrollY === 0) {
        // We're on Desktop, scroll window is `main`
        const scrollingUp = this.mainTarget.scrollTop < this.lastPosition;
        this.toggleClass(offsetCondition && scrollingUp);
        this.lastPosition = this.mainTarget.scrollTop;
      } else if (window.scrollY > 0 && this.mainTarget.scrollTop === 0) {
        // We're on mobile, scroll window is `window`
        const scrollingUp = window.scrollY < this.lastPosition;
        this.toggleClass(offsetCondition && scrollingUp);
        this.lastPosition = window.scrollY;
      }
    }
  }

  toggleClass(condition) {
    if (condition) {
      this.scrollToTopTarget.classList.add("isShown");
    } else {
      this.scrollToTopTarget.classList.remove("isShown");
    }
  }
}
