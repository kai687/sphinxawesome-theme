MASTER
~~~~~~

- feat: new option to make autodocs definitions collapsible (PR #167)
- fix: accessibility for collapsible (PR #174)
- fix: rounded search input on iOS (PR #181)

1.15.1
~~~~~~

- fix: assign nav-link only once (#166)


1.15.0
~~~~~~

- feat: modified autodocs styling
- feat: redesigned admonitions to not be in your face so much
- fix: wrongly applied padding to logo on main page
- feat: unrounded inputs, buttons, and blocks.


1.14.0
~~~~~~

- feat: switched to Material icons (#144)
- feat: mark external links (#142)
- feat: rewrite permalink behavior
- feat: use clipboard.js
- feat: HTML simplifications
- feat: CSS tooltips
- feat: better code blocks (#153)
- feat: moved things from postprocess into translator (#154)
- fix: unwanted rounding of elements (#147)
- fix: better navigation menu (#130)


1.13.1
~~~~~~

- fix: modified linenumber styling to work with new Sphinx (#123)


1.13.0
~~~~~~

- feat: better code-block directive with support for added/removed lines
- fix: remove outline-none
- docs: major update
- chore: made JavaScript and CSS more modular


1.12.1
~~~~~~

- fix: wrong link title in skip to content link


1.12.0
~~~~~~

- fix: better autodoc styling
- feat: add command line option styles
- feat: better collapsible navigation (#102)
- feat: skip to content link (#109)


1.11.0
~~~~~~

- fix: table caption number style (#96)
- fix: iOS nav menu close button fix (#65)
- feat: improve autodoc styling (#39)
- docs: add autodoc example

1.10.5
~~~~~~

- fix: python extensions run only for HTML builders (#95)
- chore: basic unit testing

1.10.4
~~~~~~

- fix: admonition ids were still problematic in LaTeX builds

1.10.3
~~~~~~

- fix: non-existing section titles no longer crash admonition_id

1.10.2
~~~~~~

- fix: non-existing image captions no longer crash HTML build (#93)

1.10.1
~~~~~~

- feat: make headerlinks accessible by keyboard (#91)
- fix: let current navigation elements stay expanded when tabbing

1.10.0
~~~~~~

- feat: make navigation elements accessible by keyboard
- feat: implement scrollspy for navigation (#70)
- fix: remove background for non-current navigation elements (#72)
- fix: list markers showing up in the search-results (#71)

1.9.0
~~~~~

- more semantic elements (``div.section`` -> ``section``, ``div.figure`` -> ``figure``, etc.)
- feat: collapsible navigation links
- chore: moved static DOM manipulation to new post-processing code in Python (#62)

1.8.0
~~~~~

- fix: improvements for search pane (#53)
- feat: add permalinks to admonitions (#58)
- fix: moved some permalink manipulation from JavaScript to Python
- fix: migrate menu state transitions to data-attributes (#55)

1.7.0
~~~~~

- feat: added auto-enabling of sampdirective extension
- feat: re-design

1.6.3
~~~~~

- fix: added styles for on-page TOC (#38)
- fix: clicking on current page links closes nav menu (#42)
- chore: moved to ``src`` package layout
- chore: added nox for automation control
- chore: added Github actions for some linting
- chore: added stylelint to lint CSS files
- chore: added eslint for linting JavaScript
- chore: added vale for simple style checks

1.6.2
~~~~~

- fix: title in menu pane also leads back to homepage (#36)
- fix: improved search input on iOS (#1)
- fix: improved search input width on wider screens

1.6.1
~~~~~

- fix(footer): justify-center
- fix(footer): made sticky (again?) (#32)
- fix(layout): improve layout on large screens (#31)
- fix: replace '-' with '|' in <title> (#33)

1.6.0
~~~~~

- fix: snackbar looks different for message vs. action (#30)
- fix: added 'print:' media-query to tailwind config
- feat: made permalinks more semantic
- feat: added directive for highlighting placeholder variables (#15)

1.5.0
~~~~~

- feat: clicking on permalink copies the link to clipboard (#29)

1.4.1
~~~~~

- fix: make bold text medium (#28)
- fix: improved padding in linenumber display

1.4.0
~~~~~

- fix: showing linenumbers for code blocks (#18)
- fix: make copy button for literals stick (#22)
- feat: add precss for nesting CSS
- feat: make prompt character unselectable (#20)
- feat: add 'breadcrumbs_separator' option (#25)
- feat: enable 'show_breadcrumbs' option (#24)
- feat: enable 'nav_show_hidden' by default (#23)
- feat: enable not showing of nav menu (#21)
- feat: added styling for code block captions (#19)
- feat: added styling for literal blocks (#17)
- fix: removed dependency on Roboto semibold (#14)
- docs: restructuring, adding more install instructions

1.3.1
~~~~~

- fix: include only used fonts (#12)

1.3.0
~~~~~

- feature: focus on search input when pressing '/' key
- feature: add project title to HTML header
- feature: support different permalinks (#8)
- fix: make nav links normal (#4)
- fix: made footer sticky (#6)

1.2.0
~~~~~

- Added styles for more admonitions
- Added styles for "rubric" heading level and TOC captions
- Fixed alignment bug for "copyright" info on small screens
- Refactored docs

1.1.0
~~~~~

- Added translatable strings throughout the theme
- Added option to override styles

1.0.1
~~~~~

- Added better labels to buttons

1.0.0
~~~~~

- Initial release
