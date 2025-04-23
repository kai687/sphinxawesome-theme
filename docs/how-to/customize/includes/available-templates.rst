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
   This template extends the template ``layout.html``.

``layout.html``
   Main template defining the structure of the page, including the HTML ``<head>`` with all imported CSS and JavaScript files.

For more information, see the available templates in the directory `src/sphinxawesome_theme`_.


.. _`src/sphinxawesome_theme`: https://github.com/kai687/sphinxawesome-theme/tree/main/src/sphinxawesome_theme
