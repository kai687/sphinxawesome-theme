import "../css/styles.css";
import "@fontsource/roboto/latin-400.css";
import "@fontsource/roboto/latin-400-italic.css";
import "@fontsource/roboto/latin-500.css";
import "@fontsource/roboto/latin-500-italic.css";
import "@fontsource/jetbrains-mono/latin-400.css";
import "@fontsource/jetbrains-mono/latin-400-italic.css";
import "@fontsource/jetbrains-mono/latin-500.css";
import "@fontsource/jetbrains-mono/latin-500-italic.css";

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
