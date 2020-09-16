import "./css/styles.css";
import "./css/fonts.css";
import { navFunctions, collapsibleNav } from "./js/nav";
import { searchPane, clearSearchHighlights, searchEvents } from "./js/search";
import { tooltipEvents } from "./js/tooltip";
import { scrollActive } from "./js/scroll";
import { copyEvents } from "./js/copy";

navFunctions();
searchPane();
clearSearchHighlights();
searchEvents();
tooltipEvents();
copyEvents();
collapsibleNav();
scrollActive();
