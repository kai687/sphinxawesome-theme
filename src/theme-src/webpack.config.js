const ESLintPlugin = require("eslint-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const RemoveEmptyScriptsPlugin = require("webpack-remove-empty-scripts");
const StyleLintPlugin = require("stylelint-webpack-plugin");
const path = require("path");
const webpack = require("webpack");

const THEME_STATIC_DIR = path.resolve(
  __dirname,
  "../sphinxawesome_theme/static/",
);

const mode = process.env.NODE_ENV || "development";
const production = mode === "production";

/** @type {import('webpack').Config} */
module.exports = {
  mode: mode,
  entry: {
    theme: "./js/app.js",
    "awesome-docsearch": "./css/docsearch.css",
    "awesome-sphinx-design": "./css/sphinx-design.css",
  },
  output: {
    path: THEME_STATIC_DIR,
    publicPath: "",
    filename: "[name].js",
    clean: production ? true : false,
  },
  plugins: [
    new ESLintPlugin({
      failOnWarning: true,
      failOnError: true,
      files: "./js/*.js",
      fix: true,
    }),
    new MiniCssExtractPlugin({
      filename: "[name].css",
    }),
    new RemoveEmptyScriptsPlugin(),
    new StyleLintPlugin({
      files: "css/*.css",
      fix: true,
    }),
    new webpack.DefinePlugin({
      "process.env": {
        NODE_ENV: JSON.stringify(process.env.NODE_ENV),
      },
    }),
  ],
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          { loader: "css-loader", options: { importLoaders: 1 } },
          "postcss-loader",
        ],
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        type: "asset/resource",
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: {
          presets: [["@babel/preset-env", { targets: "> 1%, not dead" }]],
        },
      },
      {
        test: /\.js_t$/,
        type: "asset/resource",
      },
    ],
  },
};
