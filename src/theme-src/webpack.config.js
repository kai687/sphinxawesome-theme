const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const CopyPlugin = require("copy-webpack-plugin");
const ESLintPlugin = require("eslint-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const path = require("path");
const StyleLintPlugin = require("stylelint-webpack-plugin");
const webpack = require("webpack");
const { WebpackManifestPlugin } = require("webpack-manifest-plugin");

const THEME_STATIC_DIR = path.resolve(
  __dirname,
  "../sphinxawesome_theme/static/"
);

module.exports = {
  mode: process.env.NODE_ENV || "development",
  entry: {
    theme: "./js/app.js",
    docsearch: "./js/search.js",
  },
  output: {
    path: THEME_STATIC_DIR,
    publicPath: "",
    filename: "[name].[contenthash].js",
  },
  plugins: [
    new webpack.ProgressPlugin(),
    new CleanWebpackPlugin(),
    new ESLintPlugin({
      failOnWarning: true,
      failOnError: true,
      files: "./js/*.js",
      fix: true,
    }),
    new MiniCssExtractPlugin({
      filename: "[name].[contenthash].css",
    }),
    new StyleLintPlugin({
      files: "css/*.css",
      fix: true,
    }),
    new WebpackManifestPlugin({
      basePath: "_static/",
      publicPath: "_static/",
    }),
    new webpack.DefinePlugin({
      "process.env": {
        NODE_ENV: JSON.stringify(process.env.NODE_ENV),
      },
    }),
    new CopyPlugin({
      patterns: [{ from: "./js/docsearch_config.js_t", to: THEME_STATIC_DIR }],
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
