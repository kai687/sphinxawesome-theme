const purgecss = require("@fullhuman/postcss-purgecss")({
  content: ["../sphinxawesome_theme/*.html", "./src/theme-src.js"],
  defaultExtractor: (content) => content.match(/[\w-:/]+(?<!:)/g) || [],
});

const mode = "production";
// const mode = "development"

module.exports = {
  plugins: [
    require("postcss-import"),
    require("precss"),
    require("tailwindcss"),
    require("autoprefixer"),
    mode === "production" ? purgecss : null,
    mode === "production" ? require("cssnano") : null,
  ],
};
