// scroll events
import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = ["scrollToTop", "main"];

  initialize() {
    const sections = document.querySelectorAll("article section");
    const options = {
      root: this.element,
      rootMargin: "0px 0px -95% 0px",
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        const matchingLink = document.querySelector(
          `.nav-toc a[href*=${entry.target.id}]`,
        );

        if (entry.isIntersecting && matchingLink) {
          matchingLink.classList.add("current");
        } else if (matchingLink) {
          matchingLink.classList.remove("current");
        }
      });
    }, options);

    sections.forEach((section) => {
      observer.observe(section);
    });
  }

  scrollToTop() {
    this.mainTarget.scrollTop = 0;
    window.scrollTo(0, 0);
    this.scrollToTopTarget.blur();
  }

  showButton() {
    if (this.hasScrollToTopTarget) {
      const target = this.scrollToTopTarget;

      if (this.mainTarget.scrollTop > 100 || window.scrollY > 100) {
        target.classList.add("isShown");
      } else {
        target.classList.remove("isShown");
      }
    }
  }
}
