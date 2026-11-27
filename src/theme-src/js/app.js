import "@fontsource/jetbrains-mono/latin-400-italic.css";
import "@fontsource/jetbrains-mono/latin-400.css";
import "@fontsource/jetbrains-mono/latin-500-italic.css";
import "@fontsource/jetbrains-mono/latin-500.css";
import "@fontsource/jetbrains-mono/latin-700-italic.css";
import "@fontsource/jetbrains-mono/latin-700.css";
import "../css/styles.css";

import { addCodeButtons } from "./code.js";
import { initScrollspy } from "./scrollspy.js";
import {
	initHeaderLinks,
	initNav,
	initScrollTop,
	initSearchShortcut,
	initSidebar,
	initTheme,
} from "./ui.js";

window.addEventListener("DOMContentLoaded", () => {
	initTheme();
	initSidebar();
	initNav();
	initHeaderLinks();
	initScrollTop();
	initSearchShortcut();
	addCodeButtons();
	initScrollspy();
});
