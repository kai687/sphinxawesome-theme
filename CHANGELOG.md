## 5.0.0-beta.2 (2023-05-23)

### Feat

- export permalinks icon (#1345)

### Docs

- add back umami analytics (#1328)

### Refactor

- **highlighting**: extract method for getting line numbers (#1331)
- **highlighting**: Make AwesomeCodeBlock directive shorter (#1330)
- **highlighting**: simplify (#1329)

## 5.0.0-beta.1 (2023-05-12)

### Feat

- complete redesign (#1309)

## 4.1.0 (2023-05-12)

### Feat

- use Tailwind's variables (#1298)
- restyle everything (#1292)
- sphinx-design support (#1290)
- remove html_collapsible_definitions (#1288)
- add feedback widget (#1272)
- extrahead  (#1267)
- docsearch improvements (#1264)

### Fix

- scroll to top on mobile (#1297)
- simplify controllers (#1296)
- back to top behavior (#1295)
- disable builtin search when using DocSearch (#1294)
- **styles**: improvements (#1291)
- more events (#1274)
- style issues (#1273)
- better override for page.html (#1269)
- styles (#1265)

## 4.0.3 (2023-04-16)

### Fix

- canonical links (#1262)
- canonical links (#1258)
- update (#1249)
- remove isort from dependencies (#1216)

## 4.0.2 (2023-03-05)

### Feat

- add ruff linter (#1213)

### Fix

- restore logo in header (#1215)

## 4.0.1 (2023-03-05)

### Fix

- layout issue (#1212)
- favicon (#1207)

## 4.0.0 (2023-03-01)

### Fix

- update packages (#1085)
- update packages (#1084)
- remove z-index from code copy (#1077)

## 3.3.7 (2022-09-26)

### Fix

- skip to content link (#1076)

## 3.3.6 (2022-09-23)

### Fix

- overscroll bug (#1069)

## 3.3.5 (2022-09-18)

### Feat

- testing (#1056)
- release action (#1052)

### Fix

- better print styles (#1066)
- layout (#1065)
- docsearch on mobile (#1064)
- z-index issue (#1057)

## 3.3.4 (2022-09-15)

### Fix

- docsearch (#1051)
- docsearch (#1050)

## 3.3.3 (2022-09-15)

### Fix

- docsearch preconnect (#1048)

## 3.3.2 (2022-09-15)

### Fix

- highlighting (#1046)
- highlighting inline code (#1045)
- theme works without setting extension (#1042)
- typo in update (#951)

## 3.3.1 (2022-06-13)

### Feat

- readability scores (#929)

### Fix

- update packages (#946)
- **styles**: adjust docsearch color (#927)
- **style**: adjust h1 size (#926)
- **css**: docsearch keys styling (#922)
- smaller li spacing (#807)
- scroll to top bug (#798)
- bug when not using DocSearch (#782)
- close sidebar action (#780)

## 3.3.0 (2022-02-15)

### Feat

- extra headerlinks with icons (#766)

### Fix

- code block tweaks (#775)
- allow terminal session (#772)
- make header a bit smaller (#770)
- nox and poetry (#767)
- make navlinks bigger (#760)

## 3.2.3 (2022-01-13)

## 3.2.2 (2022-01-09)

### Feat

- update to Tailwind 3.0 (#685)

## 3.2.1 (2021-11-29)

### Fix

- footnote styles (#668)

## 3.2.0 (2021-11-26)

### Feat

- support viewcode extension (#666)

## 3.1.1 (2021-11-22)

### Fix

- meta check (#663)

## 3.1.0 (2021-11-22)

### Feat

- add docsearch (#597)

### Fix

- release workflow (#661)
- bugfix when language is undefined (#660)
- **seo**: canonical links (#650)
- JSON serializer (#610)
- update netlify build image (#598)

## 3.0.0 (2021-09-02)

### Feat

- keyboard navigation in sidebar (#566)
- rethink responsive design (#559)
- additional links in the header (#553)
- add asset hashing (#550)
- add sitemaps (#539)

### Fix

- layout issues (#569)
- style tweaks (#564)
- inline code font size (#563)
- focus behavior search (#562)
- sidebar caption (#558)
- code block styles (#552)
- previous_next links style (#549)
- breadcrumbs and footer margins (#548)
- add noopener nofollow (#544)
- forgot closing emphasis tags (#543)
- remove right padding from code blocks (#542)
- search styles and revert Sphinx change (#541)
- add back click to copy (#540)
- rename (#538)
- remove headerlink logic (#537)
- adjust headerlink sizes (#535)

## 2.0.2 (2021-07-25)

### Fix

- remove duplicate stylesheets (#521)
- actions path (#511)
- linebreaks in update (#502)

## 2.0.1 (2021-07-18)

### Feat

- add vale action (#498)

## 2.0.0 (2021-06-13)

### Fix

- style for guilabel was missing (fixes #376) (#380)

## 1.19.2 (2021-02-27)

### Fix

- tests for headerlinks mechanism (#337)

## 1.19.1 (2021-01-30)

### Fix

- search with Sphinx 3.4 (#302)

## 1.19.0 (2021-01-12)

### Feat

- add support for different image alignment (#287)

### Fix

- prevent empty copyright (#285) (#286)

## 1.18.0 (2020-12-07)

### Feat

- add previous/next links (#244)
- add styles for 'diff' highlighting (#230)

### Fix

- skip to content link (#243)

## 1.17.0 (2020-11-14)

### Feat

- add copy button to all literal blocks (#216)

### Fix

- deduplicate search.html and main.html (#211) (#214)
- change of tag and filenames (closes #202) (#210)
- expand-more buttons (#209)

## 1.16.1 (2020-11-08)

### Fix

- better testing for headerlinks (#201)
- bug in headerlink mechanism (issue 198) (#199)
- admonition IDs (#197)

## 1.16.0 (2020-11-03)

### Feat

- add style for blockquotes (#189) (#192)
- make collapsible accessible
- skip collapsibles for empty definitions
- make collapsible optional
- move collapsible autodocs to html_translator
- add central icon location
- collapsible autodocs prototype

### Fix

- missing implementation for headerlinks (#193) (#194)
- styles for contents directive (#191)
- inconsistent padding (close issue #187) (#188)
- search pane appearance (fix #170) (#181)
- search pane appearance (fix #170)
- collapsible aria-label (fix #172) (#174)

## 1.15.1 (2020-10-29)

### Fix

- do not postprocess HTML multiple times (#166)

## 1.15.0 (2020-10-29)

### Feat

- unrounding inputs and buttons
- rename console to shell in code block headers (close #164)
- unrounding code blocks
- admonition redesign
- better autodocs (#160)

### Fix

- higher opacity in menu screen bg
- wrong padding with logo

## 1.14.0 (2020-10-26)

### Feat

- better nav
- better code blocks
- better code blocks
- code-blocks
- register html_translator as an internal extension
- basic styling for new code blocks
- restructuring, mostly code blocks
- move methods from postprocess to translator
- CSS tooltip implementation
- add Materials icon for collapsible
- new permalink icon

### Fix

- add shadow to nav
- code block copy behavior
- update dependencies
- move tooltips for external links
- failing tests
- add # to headerlinks (fix #148)
- headerlink tooltips hide
- use text-current for admonition headerlinks
- better tooltips for headerlinks
- simplify JS a bit
- more simplifications
- more simplifications
- simplify HTML and CSS
- failing test
- hover style for icon
- failing test
- simplify font definition
- increase linewidth
- unwanted rounding of elements (fixes #147)
- failing test
- README
- tracking in <dt>; closes #124

## 1.13.1 (2020-09-20)

### Fix

- inline linenumber styles (closes #123)

## 1.13.0 (2020-09-16)

### Feat

- highlighting tweaks
- allow highlighting added/removed lines in code blocks

### Fix

- minor tweaks for highlighting style
- restructure highlighting as an (internal) extension
- minor JS config improvements
- major simplification for the highlighting code needed
- minor highlight tweaks
- pygments-2.7.0 line numbers (closes #120)
- adjust list item spacing
- link-ids in skip to content link (close #110)
- remove outline-none

## 1.12.1 (2020-09-03)

### Fix

- wrong link title in skip to content link

## 1.12.0 (2020-09-03)

### Feat

- skip to content link (closes #109)
- better collapsible
- post-processing - remove nested spans inside cross-references
- command line option styles

### Fix

- remove useless module documentation
- better collapsible
- fold in changes from collapsible branch
- right spacing nav-toc
- breadcrumbs spacing
- breadcrumbs and list style improvements
- multiple footnotes support
- add outline to copy button on focus
- revert missing header in use.rst
- include code definitions in headerlinks
- reverse tabbing for navlinks works (fix #92)
- better autodoc styles
- type in postprocess

## 1.11.0 (2020-08-17)

### Feat

- basic autodoc styling (#39)

### Fix

- skip desc admonition nodes in admonition_ids
- attempt to fix #65
- remove whitespace from buttons
- style image caption numbers (#96)
- failing unit test for after version bump

## 1.10.5 (2020-08-14)

### Fix

- python extension should only run for HTML builds (#95)

## 1.10.4 (2020-08-13)

### Fix

- admonition ids were not fixed for all cases

## 1.10.3 (2020-08-13)

### Fix

- bug in admonitions_ids

## 1.10.2 (2020-08-11)

### Fix

- non-existing figure captions do not crash HTML
- removed buggy assign action.

## 1.10.1 (2020-08-10)

### Feat

- make more links keyboard accessible
- make headerlinks keyboard focussable (#91)

### Fix

- let current navigation stay expanded when tabbing
- make headerlink unfocussable

## 1.10.0 (2020-08-09)

### Feat

- basic scrollspy implementation (#70)

### Fix

- indent levels for l2 (#88)
- added main-wrapper id in search.html
- copy button tooltip on keyboard focus
- collapsing other expanded elements when tabbed away
- make current l1 nav link bolder
- make nav links keyboard accessible (#84)
- nav link spacing (#73)
- breadcrumbs spacing (#74)
- remove background for non-current navigation links (#72)
- list markers showing in search results (#71)

## 1.9.0 (2020-07-19)

### Feat

- collapsible navs
- collapsible navigation links (#52)

### Fix

- made triangles a little lighter again
- made triangles a little lighter
- make .highlight bg-color transparent
- revert change in nav
- list spacing (#64)
- nav position absolute up to md screens (#63)

## 1.8.0 (2020-07-05)

### Feat

- more specific links for each admonition type
- add permalinks to admonitions

### Fix

- minor accessibility tweaks
- minor accessibility tweaks
- minor style tweak for dl
- migrate menu states to data-attributes (#55)
- mypy fail
- netlify build (#59)
- moved permalink manipulation to Python code
- made "home" link in nav menu untabbable
- reduced pre font-size a tiny bit
- better focus styles
- better focus styles
- made title in header a bit smaller
- slide animation for search pane
- search pane height for better ux
- improved background color for button
- removed min-height on header again. It was a mistake

## 1.7.0 (2020-06-28)

### Feat

- re-design
- auto-enable sampdirective

### Fix

- fine-tuning redesign
- minor visual tweaks
- minor visual tweaks
- added padding consistently in nav link

## 1.6.3 (2020-06-17)

### Fix

- bug in clicking on current page links
- changed width of nav menu to 1/4
- clicking on current page links closes nav menu (#42)
- add feat for .contents module reference block
- update pre-commit hooks
- bug for specifying theme in docs
- regression for TOC styling
- styles for toctree on pages (#39)

## 1.6.2 (2020-06-09)

### Fix

- rounded form fix attempt on iOS
- rounded-full search input on iOS attempt
- rounded-full search input on iOS attempt
- width of search input in header
- title in menu on small screen leads to homepage (#36)
- regularized spelling of directives

## 1.6.1 (2020-06-08)

### Feat

- listed features in docs (#34)

### Fix

- replace - with | in html title (#33)
- autoformatter being stupid
- **layout**: forgot to modify some files (#31)
- **layout**: improve layout on wide screens (#31)
- sticky footer (issue #32)
- **footer**: justify-center

## 1.6.0 (2020-06-07)

### Feat

- add styles for samp directive
- implemented samp directive as prototype
- **permalinks**: made permalinks more semantic

### Fix

- add print media query to tailwind.config.js
- **snackbar**: differentiated clear highlight

## 1.5.0 (2020-06-01)

### Feat

- clicking on permalink copies (#29)
- copy permalink

## 1.4.1 (2020-05-31)

### Fix

- bump version
- improved padding for linenumbers
- **text**: make bold text lighter

## 1.4.0 (2020-05-31)

### Feat

- add precss
- make prompt character unselectable (#20)
- add 'breadcrumbs_separator' option
- enable show_breadcrumbs option (#24)
- **conf**: enable nav_include_hidden by default
- **nav**: enable hiding (#21)
- **code**: add style for code block captions
- **code**: add styles for literal block

### Fix

- **code**: linenumbers look decent
- **code**: copy button for literals stick
- **copyright**: fix alignment if show_nav=False
- removed dependency on semibold (#14)

## 1.3.1 (2020-05-28)

### Fix

- **search**: fix placeholder text
- **js**: made tooltip disappear on scrolling
- **search**: better labeling of input

## 1.3.0 (2020-05-27)

### Feat

- **copyright**: support for more Sphinx options
- support html_add_permalinks
- **title**: add docstitle to HTML title
- **search**: focus input on pressing slash

### Fix

- **pyproject.toml**: email change
- **nav**: overflow bug. Closes issue #6
- **docs**: get year for copyright automatically
- **footer**: made footer sticky
- add max-w-2xl to search results and copyright
- **search**: changed quotes in placeholder to single

## 1.2.0 (2020-05-24)

### Feat

- refactored docs
- added further admonition styles
- **nav**: add styles for caption in toctree
- **copyright**: support for more Sphinx options
- support html_add_permalinks
- **title**: add docstitle to HTML title
- **search**: focus input on pressing slash
- refactored docs
- added further admonition styles
- **nav**: add styles for caption in toctree

### Fix

- **caption**: fix caption in toctree
- **copyright**: margins on small devices
- **__init__**: added return statement to setup
- **__init__**: added return statement to setup
- added metadata to index page
- removed dependency on semibold (#14)
- **search**: fix placeholder text
- **fonts**: improved font handling
- **js**: made tooltip disappear on scrolling
- **search**: better labeling of input
- **pyproject.toml**: email change
- **nav**: overflow bug. Closes issue #6
- **docs**: get year for copyright automatically
- **footer**: made footer sticky
- add max-w-2xl to search results and copyright
- **search**: changed quotes in placeholder to single
- removed test directory from git
- **nav**: toc caption further tweaks
- **copyright**: margins on small devices
- **__init__**: added return statement to setup
- added metadata to index page

## 1.1.0 (2020-05-23)

### Feat

- allow adding additional CSS files
- added translatable strings

### Fix

- **search-pane**: capitalization

## 1.0.1 (2020-05-23)

### Fix

- added Changelog
- **input**: removed aria-expanded

## 1.0.0 (2020-05-20)

### Fix

- **search-pane**: capitalization
- added Changelog
- **input**: removed aria-expanded
