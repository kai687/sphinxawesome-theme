import "../css/styles.css";
import { toggleSidebar, collapsibleNav } from "./nav";
import { searchPane, clearSearchHighlights, searchEvents } from "./search";
import { scrollActive } from "./scroll";
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
  collapsible();
});
