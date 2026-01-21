const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const RemoveEmptyScriptsPlugin = require("webpack-remove-empty-scripts");
const path = require("node:path");
const { EsbuildPlugin } = require("esbuild-loader");

const THEME_STATIC_DIR = path.resolve(
	__dirname,
	"../sphinxawesome_theme/static/",
);

/** @type {import('webpack').Config} */
module.exports = {
	mode: "production",
	entry: {
		theme: "./js/app.js",
		"awesome-docsearch": "./css/docsearch.css",
		"awesome-sphinx-design": "./css/sphinx-design.css",
		"awesome-myst-nb": "./css/myst-nb.css",
	},
	output: {
		path: THEME_STATIC_DIR,
		publicPath: "",
		filename: "[name].js",
		clean: true,
	},
	optimization: {
		minimizer: [
			new EsbuildPlugin({
				target: "es2020",
			}),
		],
	},
	plugins: [
		new MiniCssExtractPlugin({
			filename: "[name].css",
		}),
		new RemoveEmptyScriptsPlugin(),
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
				loader: "esbuild-loader",
				options: {
					target: "es2020",
				},
			},
			{
				test: /\.js_t$/,
				type: "asset/resource",
			},
		],
	},
};
