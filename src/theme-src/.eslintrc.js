module.exports = {
  extends: ['eslint:recommended', 'prettier', 'plugin:tailwindcss/recommended'],
  plugins: ['tailwindcss'],
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    ecmaVersion: 6,
    sourceType: 'module',
  },
  globals: {
    _: 'readable',
    Documentation: 'readable',
  },
}
