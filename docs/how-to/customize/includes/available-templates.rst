Available templates
~~~~~~~~~~~~~~~~~~~

You can extend these main templates:

``header.html``
   Template for the header.

``footer.html``
   Template for the footer.

``page.html``
   Template for the body of the page.

   This template extends the template ``layout.html``.
   This template **must** contain the ``{{ body }}`` expression.
   The expression renders the contents of your documentation.

``layout.html``
   Main template. It defines the structure of the page, including the HTML ``<head>`` with all imported CSS and JavaScript files.

You can also override these partial templates.
The main templates include them:

``sidebar.html``
   Template for the left sidebar.
   It includes the templates from the :confval:`sphinx:html_sidebars` setting.

``sidebar_toc.html``
   Template for the links to your documentation pages in the left sidebar.

``sidebar_main_nav_links.html``
   Template for the main navigation links in the left sidebar on small screens.

``toc.html``
   Template for the on-page table of contents in the right sidebar.
   It has the blocks ``toc_before`` and ``toc_after``.
   These blocks add content before and after the table of contents.

``breadcrumbs.html``
   Template for the breadcrumbs above the page content.

``prev_next.html``
   Template for the links to the previous page and the next page.

``searchbox.html``
   Template for the search box in the header.

``scrolltop.html``
   Template for the button that scrolls to the top of the page.

For more information, read the templates in the directory `src/sphinxawesome_theme`_.


.. _`src/sphinxawesome_theme`: https://github.com/kai687/sphinxawesome-theme/tree/main/src/sphinxawesome_theme
