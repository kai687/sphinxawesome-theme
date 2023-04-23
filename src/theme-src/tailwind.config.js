const colors = require("tailwindcss/colors");

module.exports = {
  corePlugins: {
    animation: false,
    container: false,
  },
  content: ["../sphinxawesome_theme/*.html", "./js/**/*.js"],
  safelist: ["lead", "rubric", "centered"],
  theme: {
    fontFamily: {
      sans: ["Roboto", "sans-serif"],
      mono: ["JetBrains\\ Mono", "monospace"],
    },
    fontSize: {
      xs: [".75rem", "1.5"],
      sm: [".875rem", "1.5"],
      code: [".9375em", "1.5"],
      base: ["16px", "1.5"],
      m: ["1.125rem", "1.5"],
      lg: ["1.375rem", "1.2"],
      xl: ["1.5rem", "1.2"],
      "2xl": ["1.75rem", "1.2"],
      "3xl": ["2.5rem", "1.2"],
      "4xl": ["3rem", "1.2"],
      "5xl": ["3.125rem", "1.2"],
      "6xl": ["3.75rem", "1.2"],
    },
    extend: {
      listStyleType: {
        latin: "lower-latin",
      },
      screens: {
        print: { raw: "print" },
      },
      maxWidth: {
        prose: "760px",
      },
      lineHeight: {
        14: "3.5rem",
      },
      margin: {
        fluid: "var(--fluid-margin)",
      },
      width: {
        sidebar: "max(var(--sidebar-width), 17%)",
      },
      colors: {
        blue: colors.sky,
        brand: "var(--color-brand)",
        link: "var(--color-link)",
        gray: {
          light: "var(--color-gray-light)",
          DEFAULT: "var(--color-gray)",
          dark: "var(--color-gray-dark)",
        },
      },
    },
  },
};
