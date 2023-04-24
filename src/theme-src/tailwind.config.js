const colors = require("tailwindcss/colors");

module.exports = {
  corePlugins: {
    animation: false,
    container: false,
  },
  content: ["../sphinxawesome_theme/*.html", "./js/**/*.js"],
  safelist: ["headerlink"],
  plugins: [require("@tailwindcss/typography")],
  theme: {
    fontFamily: {
      sans: ["Roboto", "sans-serif"],
      mono: ["JetBrains\\ Mono", "monospace"],
    },
    fontSize: {
      xs: ".75rem", // lineHeight: 1.5
      sm: ".875rem", // lineHeight: 1.5
      code: ".9375em", // lineHeight: 1.5
      base: "16px", // lineHeight: 1.5
      m: "1.125rem", // lineHeight: 1.5
      lg: "1.375rem", //lineHeight: "1.2"
      xl: "1.5rem", // lineHeight: "1.2"
      "2xl": "1.75rem", // lineHeight: "1.2"
      "3xl": "2.5rem", // lineHeight: "1.2"
      "4xl": "3rem", // lineHeight: "1.2"
      "5xl": "3.125rem", // lineHeight: "1.2"
      "6xl": "3.75rem", // lineHeight: "1.2"
    },
    extend: {
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
        brand: "var(--color-brand)",
        link: "var(--color-link)",
        gray: {
          light: "var(--color-gray-light)",
          DEFAULT: "var(--color-gray)",
          dark: "var(--color-gray-dark)",
        },
      },
      typography: ({ theme }) => ({
        DEFAULT: {
          css: [
            {
              color: "inherit",
              lineHeight: "inherit",
              maxWidth: theme("maxWidth.prose"),
              svg: {
                display: "inline",
              },
              strong: {
                fontWeight: theme("fontWeight.medium"),
              },
              h1: {
                marginTop: theme("spacing.20"),
                color: theme("colors.gray.dark"),
                fontSize: theme("fontSize.3xl"),
                letterSpacing: theme("letterSpacing.tight"),
                fontWeight: theme("fontWeight.normal"),
              },
              h2: {
                fontSize: theme("fontSize.2xl"),
                letterSpacing: theme("letterSpacing.tight"),
                color: theme("colors.gray.dark"),
                fontWeight: theme("fontWeight.normal"),
              },
              h3: {
                fontSize: theme("fontSize.lg"),
                fontWeight: theme("fontWeight.normal"),
                color: theme("colors.gray.dark"),
              },
              h4: {
                fontWeight: theme("fontWeight.medium"),
                color: theme("colors.gray.dark"),
              },
              ".rubric": {
                fontWeight: theme("fontWeight.medium"),
                color: theme("colors.gray.dark"),
                marginBottom: "0.5em",
              },
              ".centered": {
                textAlign: "center",
              },
              ".lead": {
                color: theme("colors.gray.dark"),
              },
              ".lead + *": {
                marginTop: theme("spacing.12"),
              },
              a: {
                color: theme("colors.link"),
                fontWeight: theme("fontWeight.normal"),
                textDecoration: "none",
              },
              "a:hover": {
                color: theme("colors.brand"),
                textDecoration: "underline",
              },
              "a:focus": {
                color: theme("colors.brand"),
                textDecoration: "underline",
              },
              "ol > li::marker": {
                fontWeight: theme("fontWeight.medium"),
                color: theme("colors.gray.dark"),
              },
              "ol ol": {
                listStyle: "lower-latin",
              },
              "ul > li::marker": {
                color: theme("colors.gray.light"),
              },
              ".samp em": {
                color: theme("colors.purple.800"),
              },
              ".file em": {
                color: theme("colors.purple.800"),
              },
              blockquote: {
                color: "inherit",
                fontWeight: theme("fontWeight.normal"),
                fontStyle: "normal",
                fontSize: theme("fontSize.sm"),
                marginTop: theme("spacing.6"),
                marginBottom: theme("spacing.6"),
                paddingLeft: theme("spacing.4"),
                padding: theme("spacing.4"),
                borderLeftWidth: "4px",
                boxShadow: theme("boxShadow.DEFAULT"),
                // bg-gray-50/30
                backGroundColor: "rgba(249,250,251,.3)",
              },
              "blockquote .attribution": {
                fontStyle: "italic",
              },
              "blockquote p:last-child": {
                marginBottom: "0",
              },
              "blockquote p:first-child": {
                marginTop: "0",
              },
              "blockquote p:first-of-type::before": {
                content: "",
              },
              "blockquote p:last-of-type::after": {
                content: "",
              },
              dt: {
                fontWeight: theme("fontWeight.medium"),
              },
              dd: {
                paddingLeft: theme("spacing.5"),
              },
              "kbd:not(.compound)": {
                display: "inline-block",
                fontSize: theme("fontSize.xs"),
                fontWeight: theme("fontWeight.medium"),
                padding: theme("spacing.1"),
                borderWidth: "1px",
                borderColor: theme("colors.gray.dark"),
                borderRadius: theme("borderRadius.sm"),
              },
              ".guilabel": {
                fontWeight: theme("fontWeight.medium"),
                color: theme("colors.gray.dark"),
                letterSpacing: theme("letterSpacing.wide"),
              },
              ".menuselection": {
                fontWeight: theme("fontWeight.medium"),
                color: theme("colors.gray.dark"),
                letterSpacing: theme("letterSpacing.wide"),
              },
              "figure img": {
                display: "inline-block",
              },
              ".align-center": {
                marginLeft: "auto",
                marginRight: "auto",
                textAlign: "center",
              },
              ".align-right": {
                marginLeft: "auto",
                textAlign: "right",
              },
              caption: {
                color: theme("colors.gray.light"),
                textAlign: "left",
                marginBottom: theme("spacing.6"),
              },
              "thead th": {
                fontWeight: theme("fontWeight.medium"),
              },
              "table p:first-child": {
                marginTop: "0",
              },
              "table p:last-child": {
                marginBottom: "0",
              },
              ".highlight": {
                position: "relative",
              },
              pre: {
                color: "inherit",
                backgroundColor: "inherit",
                borderWidth: "1px",
                borderRadius: theme("borderRadius.sm"),
                marginTop: 0,
                marginBottom: 0,
              },
              "pre mark": {
                display: "block",
                backgroundColor: theme("colors.sky.50"),
              },
              "pre ins": {
                display: "block",
                backgroundColor: theme("colors.green.50"),
                textDecoration: "none",
              },
              ".highlight-diff .gi": {
                backgroundColor: theme("colors.green.50"),
                display: "inline-block",
                width: "100%",
              },
              "pre del": {
                display: "block",
                backgroundColor: theme("colors.red.50"),
                textDecoration: "none",
              },
              ".highlight-diff .gd": {
                backgroundColor: theme("colors.red.50"),
                display: "inline-block",
                width: "100%",
              },
              ".literal-block-wrapper": {
                borderWidth: "1px",
                borderRadius: theme("borderRadius.sm"),
              },
              ".literal-block-wrapper pre": {
                border: "none",
              },
              ".pre": {
                whiteSpace: "nowrap",
                hyphens: "none",
              },
              ".code-block-caption": {
                color: theme("colors.gray.light"),
                fontSize: theme("fontSize.sm"),
                letterSpacing: theme("letterSpacing.wide"),
                borderBottomWidth: "1px",
                backgroundColor: theme("colors.gray.50"),
                borderTopLeftRadius: theme("borderRadius.sm"),
                borderTopRightRadius: theme("borderRadius.sm"),
                padding: theme("spacing.1"),
                display: "flex",
                justifyContent: "flex-end",
              },
              ".font-size-inherit": {
                fontSize: "inherit !important",
              },
              ".footnote > .label": {
                float: "left",
                paddingRight: theme("spacing.2"),
              },
              ".footnote > :not(.label)": {
                marginLeft: theme("spacing.8"),
              },
            },
          ],
        },
      }),
    },
  },
};
