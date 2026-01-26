import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import rspack from "@rspack/core";
import RemoveEmptyScriptsPlugin from "webpack-remove-empty-scripts";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const THEME_STATIC_DIR = resolve(__dirname, "../sphinxawesome_theme/static/");

/** @type {import('webpack').Config} */
export default {
	devtool: false,
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
	plugins: [
		new rspack.CssExtractRspackPlugin({
			filename: "[name].css",
		}),
		new RemoveEmptyScriptsPlugin(),
	],
	module: {
		rules: [
			{
				test: /\.css$/,
				use: [
					rspack.CssExtractRspackPlugin.loader,
					{ loader: "css-loader", options: { importLoaders: 1 } },
					"postcss-loader",
				],
				type: "javascript/auto",
			},
			{
				test: /\.(woff|woff2|eot|ttf|otf)$/,
				type: "asset/resource",
			},
			{
				test: /\.js$/,
				exclude: /node_modules/,
				loader: "builtin:swc-loader",
				options: {
					env: {
						targets: ["last 2 versions", "not dead", "not op_mini all"],
					},
				},
				type: "javascript/auto",
			},
			{
				test: /\.js_t$/,
				type: "asset/resource",
			},
		],
	},
};
