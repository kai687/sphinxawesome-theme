module.exports = {
  plugins: [
    require("postcss-import"),
    require("postcss-custom-selectors"),
    require("postcss-preset-env")({
      minimumVendorImplementations: 2,
    }),
    require("tailwindcss/nesting"),
    require("tailwindcss"),
    require("autoprefixer"),
    require("cssnano"),
  ],
};
