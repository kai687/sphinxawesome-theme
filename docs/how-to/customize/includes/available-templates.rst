Available templates
~~~~~~~~~~~~~~~~~~~

The main templates you can extend are:

``header.html``
   Template for the header.

``footer.html``
   Template for the footer.

``page.html``
   Template for the body of the page.

   This page **must** contain the ``{{ body }}`` expression to render the contents of your documentation.
   The ``page`` template extends the layout ``with-sidebar`` or ``without-sidebar`` depending on the context.

`without-sidebar.html`
   Template for a page without navigation sidebar.
   This template is used when the option ``show_nav`` is set to ``False``,
   or when you set ``layout: "without-sidebar"`` in the frontmatter of your Markdown document.
   This template extends the main template ``layout``.

``with-sidebar.html``
   Template with navigation sidebar on the left.
   This is the default template for all documentation pages.
   It extends from the main template ``layout``.

``layout.html``
   Main template defining the structure of the page, including the HTML ``<head>`` with all imported CSS and JavaScript files.

For more information, see the available templates in the directory `src/sphinxawesome_theme`_.


.. _`src/sphinxawesome_theme`: https://github.com/kai687/sphinxawesome-theme/tree/main/src/sphinxawesome_theme
