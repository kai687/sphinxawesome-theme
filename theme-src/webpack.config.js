const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  mode: "production",
  entry: {
    theme: "./src/theme-src.js"
  },
  output: {
    filename: "[name].js",
    path: path.resolve(__dirname, "../sphinxawesome_theme/static/")
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "theme.css"
    })
  ],
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          { loader: "css-loader", options: { importLoaders: 1 } },
          "postcss-loader"
        ]
      }
    ]
  }
};
