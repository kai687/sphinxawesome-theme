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
              "--tw-prose-body": "var(--color-gray)",
              "--tw-prose-headings": "var(--color-gray-dark)",
              "--tw-prose-lead": "var(--color-gray-dark)",
              "--tw-prose-links": "var(--color-link)",
              "--tw-prose-counters": "var(--color-gray-dark)",
              "--tw-prose-bullets": "var(--color-gray-light)",
              "--tw-prose-pre-code": "inherit",
              "--tw-prose-pre-bg": "inherit",
              // from Pygmentes 'github dark' theme
              "--tw-prose-invert-code": "#79c0ff",
              "--tw-prose-captions": "var(--color-gray-light)",
              "--awsm-prose-placeholders": theme("colors.purple[800]"),
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
                fontSize: theme("fontSize.3xl"),
                letterSpacing: theme("letterSpacing.tight"),
                fontWeight: theme("fontWeight.normal"),
              },
              h2: {
                fontSize: theme("fontSize.2xl"),
                letterSpacing: theme("letterSpacing.tight"),
                fontWeight: theme("fontWeight.normal"),
              },
              h3: {
                fontSize: theme("fontSize.lg"),
                fontWeight: theme("fontWeight.normal"),
              },
              h4: {
                fontWeight: theme("fontWeight.medium"),
              },
              ".rubric": {
                fontWeight: theme("fontWeight.medium"),
                color: "var(--tw-prose-headings)",
                marginBottom: "0.5em",
              },
              ".centered": {
                textAlign: "center",
              },
              ".lead + *": {
                marginTop: theme("spacing.12"),
              },
              a: {
                fontWeight: theme("fontWeight.normal"),
                textDecoration: "none",
              },
              "a.toc-backref": {
                color: "inherit",
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
              },
              "ol ol": {
                listStyle: "lower-latin",
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
                // backGroundColor: "rgba(249,250,251,.3)",
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
              dl: {
                marginBottom: theme("spacing.5"),
                marginTop: theme("spacing.5"),
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
                padding: "1px 4px",
                borderWidth: "1px",
                borderColor: theme("colors.gray.dark"),
                borderRadius: theme("borderRadius.sm"),
                boxShadow: "1px 1px",
              },
              ".option-list kbd": {
                borderWidth: 0,
                fontSize: "inherit",
                boxShadow: "none",
                fontWeight: theme("fontWeight.bold"),
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
              "code::before": {
                content: "",
              },
              "code::after": {
                content: "",
              },
              pre: {
                fontSize: theme("fontSize.code"),
                backgroundColor: "inherit",
                borderWidth: "1px",
                borderRadius: theme("borderRadius.sm"),
                marginTop: 0,
                marginBottom: 0,
              },
              "pre mark": {
                display: "block",
                backgroundColor: theme("colors.sky[50]"),
              },
              "pre ins": {
                display: "block",
                backgroundColor: theme("colors.green[50]"),
                textDecoration: "none",
              },
              "pre del": {
                display: "block",
                backgroundColor: theme("colors.red[50]"),
                textDecoration: "none",
              },
              ".highlight-diff .gi": {
                backgroundColor: theme("colors.green[50]"),
                display: "inline-block",
                width: "100%",
              },
              ".highlight-diff .gd": {
                backgroundColor: theme("colors.red[50]"),
                display: "inline-block",
                width: "100%",
              },
              ".highlight .gp": {
                pointerEvents: "none",
                userSelect: "none",
                fontWeight: theme("fontWeight.medium"),
              },
              ".highlight .linenos": {
                userSelect: "none",
                paddingRight: "1rem",
              },
              ".pre": {
                whiteSpace: "nowrap",
                hyphens: "none",
              },
              ".sig": {
                fontWeight: theme("fontWeight.bold"),
                fontFamily: "JetBrains\\ Mono",
              },
              ".sig-name": {
                color: "black",
              },
              ".default_value": {
                color: "var(--awsm-prose-placeholders)",
              },
              "em.property": {
                color: "theme(colors.gray.light)",
              },
              ".option .sig-prename": {
                fontStyle: "italic",
                color: "var(--awsm-prose-placeholders)",
              },
              ".viewcode-link": {
                float: "right",
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
        invert: {
          css: [
            {
              a: {
                textDecoration: "underline",
                textDecorationColor: "var(--color-brand)",
                textUnderlineOffset: "3px",
              },
              pre: {
                borderColor: theme("colors.gray[700]"),
                // from Pygments 'github dark' style
                backgroundColor: "#0d1117",
              },
              "pre mark": {
                backgroundColor: "#223",
              },
              "pre ins": {
                // from Pygments 'github dark' style
                backgroundColor: "#0f5323",
              },
              "pre del": {
                // from Pygments 'github dark' style
                backgroundColor: "#490202",
              },
              "kbd:not(.compound)": {
                borderColor: "#fff",
              },
            },
          ],
        },
      }),
    },
  },
};
