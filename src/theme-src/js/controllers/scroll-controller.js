// scroll events
import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  connect() {
    const sections = document.querySelectorAll("article section");
    const options = {
      root: this.element,
      rootMargin: "0px 0px -95% 0px",
    };

    // Mark the currently active section
    const observer = new IntersectionObserver(
      this._highlightCurrentSection,
      options,
    );

    sections.forEach((section) => {
      observer.observe(section);
    });
  }

  // private
  _highlightCurrentSection(entries) {
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
  }
}
