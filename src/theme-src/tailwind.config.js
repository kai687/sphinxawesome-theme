const colors = require("tailwindcss/colors");

module.exports = {
  purge: ["../sphinxawesome_theme/*.html", "./js/*.js", "./css/*.css"],
  variants: {
    extend: {
      outline: ["active"],
    },
  },
  theme: {
    fontFamily: {
      sans: ["Roboto", "sans-serif"],
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
      },
      margin: {
        fluid: "var(--fluid-margin)",
      },
      colors: {
        blue: colors.lightBlue,
      },
    },
  },
};
