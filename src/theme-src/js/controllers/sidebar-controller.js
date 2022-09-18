// Open/close the sidebar
import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = ["sidebar", "screen", "hamburger"];

  initialize() {
    this.page = this.element;

    // remove the hamburger button, if there's no sidebar
    if (!this.hasSidebarTarget) {
      this.hamburgerTarget.remove();
    }
  }

  connect() {
    if (this.hasSidebarTarget) {
      this.handleFocus();
    }
  }

  open() {
    this.page.classList.add("isShown");
    this.sidebarTarget.classList.add("isShown");
    this.screenTarget.classList.add("isShown");
    this.handleFocus();
  }

  close() {
    this.page.classList.remove("isShown");
    this.sidebarTarget.classList.remove("isShown");
    this.screenTarget.classList.remove("isShown");
    this.removeAllFocus();
  }

  expandKeyPressed(event) {
    if (event.code === "Enter" || event.code === "Space") {
      this.expand(event);
    }
  }

  // collapse/expand navigation sections
  expand(event) {
    const icon = event.currentTarget;
    const expandable = icon.parentElement.parentElement;
    expandable.classList.toggle("expanded");

    if (expandable.classList.contains("expanded")) {
      // add focus to first-generation children of `expanded` section
      expandable.parentElement
        .querySelectorAll(".expanded > ul > li > .nav-link > a")
        .forEach((link) => {
          link.setAttribute("tabindex", "0");
          this.setIconFocus(link.previousElementSibling, "0");
        });
    } else {
      // remove focus from all links below (targets the `ul`)
      icon.parentElement.nextElementSibling
        .querySelectorAll("a")
        .forEach((link) => {
          link.setAttribute("tabindex", "-1");
          this.setIconFocus(link.previousElementSibling, "-1");
        });
    }
  }

  // manage the keyboard focus in the sidebar
  handleFocus() {
    // all links that are not in an `expanded` section ...
    this.getNotExpandedLinks().forEach((link) => {
      const icon = link.previousElementSibling;

      // ... and links that are not on level 1 (those are always visible)
      if (!link.parentNode.parentNode.classList.contains("toctree-l1")) {
        // ... should not receive focus
        link.setAttribute("tabindex", "-1");
        this.setIconFocus(icon, "-1");
      } else {
        link.setAttribute("tabindex", "0");
        this.setIconFocus(icon, "0");
      }
    });
  }

  getNotExpandedLinks() {
    return this.sidebarTarget.querySelectorAll(
      ":not(.expanded) > ul > li > .nav-link > a",
    );
  }

  setIconFocus(element, tabindex) {
    if (element && element.classList.contains("expand")) {
      element.setAttribute("tabindex", tabindex);
    }
  }

  removeAllFocus() {
    this.sidebarTarget
      .querySelectorAll("a, svg")
      .forEach((item) => item.setAttribute("tabindex", "-1"));
  }
}
