import "alpinejs";
import "../css/styles.css";
import { collapsibleNav } from "./nav";
import { clearSearchHighlights, searchEvents } from "./search";
// import { scrollActive } from "./scroll";
import { copyEvents } from "./copy";
import { collapsible } from "./collapsible";

clearSearchHighlights();
searchEvents();
copyEvents();
collapsibleNav();
// scrollActive();
collapsible();
