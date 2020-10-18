const path = require("path");
const ESLintPlugin = require("eslint-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const StyleLintPlugin = require("stylelint-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const webpack = require("webpack");

module.exports = {
  mode: process.env.NODE_ENV || "development",
  entry: {
    theme: "./app.js",
  },
  output: {
    path: path.resolve(__dirname, "../sphinxawesome_theme/static/"),
    publicPath: "",
  },
  plugins: [
    new webpack.ProgressPlugin(),
    new CleanWebpackPlugin(),
    new ESLintPlugin({
      failOnWarning: true,
      failOnError: true,
      files: "./js/*.js",
    }),
    new MiniCssExtractPlugin({
      filename: "theme.css",
    }),
    new StyleLintPlugin({
      files: "css/*.css",
      fix: true,
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
        use: ["file-loader"],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: {
          presets: [
            ["@babel/preset-env", { targets: '> 1%, not dead' }]
          ]
        },
      },
    ],
  },
};
