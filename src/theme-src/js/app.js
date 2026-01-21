import "@fontsource/jetbrains-mono/latin-400-italic.css";
import "@fontsource/jetbrains-mono/latin-400.css";
import "@fontsource/jetbrains-mono/latin-500-italic.css";
import "@fontsource/jetbrains-mono/latin-500.css";
import "@fontsource/jetbrains-mono/latin-700-italic.css";
import "@fontsource/jetbrains-mono/latin-700.css";
import "../css/styles.css";

import intersect from "@alpinejs/intersect";
import persist from "@alpinejs/persist";
import Alpine from "alpinejs";
import { addCodeButtons } from "./code";

window.Alpine = Alpine;
Alpine.plugin([intersect, persist]);
Alpine.start();

window.addEventListener("DOMContentLoaded", () => {
  addCodeButtons();
});
