import "./css/styles.css";
import "./css/fonts.css";
import { navFunctions, collapsibleNav } from "./js/nav";
import { searchPane, clearSearchHighlights, searchEvents } from "./js/search";
import { scrollActive } from "./js/scroll";
import { copyEvents } from "./js/copy";
import { collapsible } from "./js/collapsible";

navFunctions();
searchPane();
clearSearchHighlights();
searchEvents();
copyEvents();
collapsibleNav();
scrollActive();
collapsible();
