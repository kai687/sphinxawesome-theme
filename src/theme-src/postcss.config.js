module.exports = {
  plugins: [
    require("postcss-import"),
    require("tailwindcss"),
    require("postcss-focus-visible"),
    require("postcss-preset-env")({ stage: 1 }),
    ...(process.env.NODE_ENV === "production" ? [require("cssnano")] : []),
  ],
};
