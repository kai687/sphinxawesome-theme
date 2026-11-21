import "@fontsource/jetbrains-mono/latin-400-italic.css";
import "@fontsource/jetbrains-mono/latin-400.css";
import "@fontsource/jetbrains-mono/latin-500-italic.css";
import "@fontsource/jetbrains-mono/latin-500.css";
import "@fontsource/jetbrains-mono/latin-700-italic.css";
import "@fontsource/jetbrains-mono/latin-700.css";
import "../css/styles.css";

import { addCodeButtons } from "./code.js";
import {
	initCollapsibleNav,
	initHeaderlinks,
	initScrollspy,
	initScrollTop,
	initSearchShortcut,
	initSidebar,
	initThemeToggle,
} from "./ui.js";

window.addEventListener("DOMContentLoaded", () => {
	addCodeButtons();
	initThemeToggle();
	initSidebar();
	initCollapsibleNav();
	initHeaderlinks();
	initScrollspy();
	initScrollTop();
	initSearchShortcut();
});
