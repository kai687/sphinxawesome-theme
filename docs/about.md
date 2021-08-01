# About

```{rst-class} lead
This page describes the external assets of the Sphinx awesome theme and topics that
didn't fit anywhere else.
```

## Assets

The Sphinx awesome theme relies on the following assets. You can find the complete list
of dependencies in the files `pyproject.toml` for Python dependencies and `package.json`
for JavaScript dependencies.

<!-- vale Awesome.SpellCheck = NO -->

| Feature                                               | Name/Website                                                             | License                                                                                      |
| ----------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| CSS framework                                         | [Tailwind]                                                               | [MIT License](https://github.com/tailwindlabs/tailwindcss/blob/master/LICENSE)               |
| Copy to clipboard                                     | [Clipboard.js](https://clipboardjs.com/)                                 | [MIT License](https://github.com/zenorocha/clipboard.js/blob/master/LICENSE)                 |
| Fonts                                                 | [Roboto](https://github.com/googlefonts/roboto)                          | [Apache License, Version 2.0]                                                                |
|                                                       | [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono/)            | [SIL Open Font License, 1.1](https://github.com/JetBrains/JetBrainsMono/blob/master/OFL.txt) |
| Icons                                                 | [Material icons](https://fonts.google.com/icons?selected=Material+Icons) | [Apache License, Version 2.0]                                                                |
| Tooltips                                              | [Primer/CSS](https://primer.style/css/)                                  | [MIT License](https://github.com/primer/css/blob/main/LICENSE)                               |
| **Note:** versions ≤ 1.13.1 used these icons instead: | [Entypo](http://www.entypo.com) by Daniel Bruce                          | [Creative Commons Attribution-ShareAlike 4.0]                                                |
|                                                       | [Zondicons](http://www.zondicons.com) by Steve Schoger                   | ?                                                                                            |

<!-- vale Awesome.SpellCheck = YES -->

[creative commons attribution-sharealike 4.0]: https://creativecommons.org/licenses/by-sa/4.0/legalcode
[apache license, version 2.0]: https://www.apache.org/licenses/LICENSE-2.0.html

The icons are included as inline SVG in the HTML templates. [Webpack] copies the fonts
into the theme's static directory. The CSS for the tooltips are in the file
`tooltips.css` and adapted for Tailwind.

## How does it work?

Sphinx themes are a collection of HTML templates, CSS styles, and JavaScript files.
Sphinx uses the [Jinja2] templating language. The main template is in the file
`layout.html`. It defines the overall structure of the page and imports other parts,
such as the header or navigation menu. The template file `page.html` is inherited from
Sphinx's basic theme. It extends the main `layout.html` template and renders the `body`
text.

The Sphinx awesome theme defines a few internal extensions, that add features like the
code blocks. An HTML postprocessing extension using [BeautifulSoup] changes the HTML
when modifying the Sphinx/docutils toolchain is too cumbersome.

## Package and project management

The project is distributed as a Python package. The following tools are vital to
achieve this:

- [Poetry](https://python-poetry.org/)
- [Nox](https://nox.thea.codes/en/stable/)
<!-- vale 18F.Clarity = NO -->
- [pre-commit](https://pre-commit.com/)
<!-- vale 18F.Clarity = YES -->

[Webpack] manages the JavaScript and CSS portions of the theme. The entry point for
webpack is the file `app.js`. All dependencies are imported here, including fonts and
CSS.

See the Webpack configuration file `webpack.config.js` for the full pipeline.

[jinja2]: https://jinja.palletsprojects.com
[webpack]: https://webpack.js.org
[tailwind]: https://tailwindcss.com
[docutils]: https://docutils.sourceforge.io/
[beautifulsoup]: https://www.crummy.com/software/BeautifulSoup/
