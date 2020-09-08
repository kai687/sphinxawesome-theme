const mode = "production";

module.exports = {
  plugins: [
    require("postcss-import"),
    require("precss"),
    require("tailwindcss"),
    require("autoprefixer"),
    mode === "production" ? require("cssnano") : null,
  ],
};
