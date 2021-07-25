import "../css/styles.css";

import { Application } from "stimulus"
import { definitionsFromContext } from "stimulus/webpack-helpers"

const app = Application.start()
const ctx = require.context("./controllers", true, /.js$/)

app.load(definitionsFromContext(ctx))
