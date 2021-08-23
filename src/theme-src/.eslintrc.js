module.exports = {
  extends: ["eslint:recommended", "plugin:prettier/recommended"],
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    ecmaVersion: 6,
    sourceType: "module",
  },
  globals: {
    _: "readable",
    Documentation: "readable",
  },
};
