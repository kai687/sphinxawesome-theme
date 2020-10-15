module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
    standardFontWeights: true,
    defaultLineHeights: true,
  },
  purge: ["../sphinxawesome_theme/*.html", "./js/*.js", "./css/*.css"],
  theme: {
    fontFamily: {
      display: ["Roboto", "sans-serif"],
      body: ["Roboto", "sans-serif"],
      mono: ["Roboto\\ Mono", "monospace"],
    },
    listStyleType: {
      none: "none",
      disc: "disc",
      decimal: "decimal",
      square: "square",
      latin: "lower-latin",
    },
    extend: {
      screens: {
        print: { raw: "print" },
        xxl: "1440px",
      },
      padding: {
        18: "4.5rem",
      },
    },
  },
};
