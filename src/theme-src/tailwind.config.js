const colors = require("tailwindcss/colors");

module.exports = {
  corePlugins: {
    animation: false,
  },
  mode: "jit",
  purge: ["../sphinxawesome_theme/*.html", "./js/**/*.js"],
  variants: {
    extend: {
      outline: ["active"],
      translate: ["active"],
      textColor: ["group-focus", "focus-visible"],
    },
  },
  theme: {
    fontFamily: {
      sans: ["Roboto", "sans-serif"],
      mono: ["JetBrains\\ Mono", "monospace"],
      // mono: ["Roboto\\ Mono", "monospace"],
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
      },
      margin: {
        fluid: "var(--fluid-margin)",
      },
      colors: {
        blue: colors.sky,
        brand: "var(--color-brand)",
        link: "var(--color-link)",
      },
      borderRadius: {
        xs: "1px",
      },
      backgroundOpacity: {
        "2": "0.02",
      },
    },
  },
};
