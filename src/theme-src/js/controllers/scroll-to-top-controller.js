// Scroll to top button
import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = ["scrollToTop"];

  connect() {
    this.scrollWindow = this.element;
    this.lastPosition = 0;
    this.offset = 200;
  }

  scroll() {
    this.scrollWindow.scrollTop = 0;
    window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
    this.scrollToTopTarget.blur();
  }

  showButton() {
    if (this.hasScrollToTopTarget) {
      const offsetCondition = this.scrollWindow.scrollTop > this.offset;
      const scrollingUp = this.scrollWindow.scrollTop < this.lastPosition;
      if (offsetCondition && scrollingUp) {
        this.scrollToTopTarget.classList.add("isShown");
      } else {
        this.scrollToTopTarget.classList.remove("isShown");
      }
    }
    this.lastPosition = this.scrollWindow.scrollTop;
  }
}
