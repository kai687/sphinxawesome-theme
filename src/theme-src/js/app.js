import "../css/styles.css";
import { collapsibleNav } from "./nav";
import { toggleSidebar } from "./sidebar";
import { searchPane, clearSearchHighlights, searchEvents } from "./search";
import { scrollActive, scrollToTop } from "./scroll";
import { copyEvents } from "./copy";
import { collapsible } from "./collapsible";

window.addEventListener("DOMContentLoaded", () => {
  toggleSidebar();
  searchPane();
  clearSearchHighlights();
  searchEvents();
  copyEvents();
  collapsibleNav();
  scrollActive();
  scrollToTop();
  collapsible();
});
