module.exports = {
  plugins: [
    require("postcss-import"),
    require("precss"),
    require("tailwindcss"),
    require("autoprefixer"),
    ...(process.env.NODE_ENV === "production" ? [require("cssnano")] : []),
  ],
};
