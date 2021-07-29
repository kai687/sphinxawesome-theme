import "../css/styles.css";
import "@fontsource/roboto/latin-400.css";
import "@fontsource/roboto/latin-400-italic.css";
import "@fontsource/roboto/latin-500.css";
import "@fontsource/roboto/latin-500-italic.css";
import "@fontsource/jetbrains-mono/latin-400.css";
import "@fontsource/jetbrains-mono/latin-400-italic.css";
import "@fontsource/jetbrains-mono/latin-500.css";
import "@fontsource/jetbrains-mono/latin-500-italic.css";

import { Application } from "stimulus"
import { definitionsFromContext } from "stimulus/webpack-helpers"

const app = Application.start()
const ctx = require.context("./controllers", true, /.js$/)

app.load(definitionsFromContext(ctx))
