Add custom templates
~~~~~~~~~~~~~~~~~~~~

You can define completely custom layouts and templates for your pages.

For example, to create your own custom footer template,
create a file :file:`_templates/footer.html` with the following content:

.. code-block:: html+jinja
   :caption: File: _tempates/footer.html

   {# A custom footer template that doesn't inherit from the parent. #}

   <div style="background-color: red;">
      Your custom footer.
   </div>

.. seealso::

   :ref:`sec:add-custom-templates`

Add custom page layouts
~~~~~~~~~~~~~~~~~~~~~~~


Instead of overriding the global page layout,
you can add create custom layouts that are only used on individual pages.

.. important::

   You can only select per-page layouts if you write your documentation in Markdown
   using the `myst-parser <https://myst-parser.readthedocs.io/en/latest/index.html>`_ extension.

To create a custom layout, create a new file :file:`_templates/custom-layout.html`:

.. code-block:: html+jinja
   :caption: File: _templates/custom-layout.html

   <html>
      <body>{{ body }}</body>
   </html>

Then, in your Markdown document, select your layout using the ``layout`` option in the YAML frontmatter:


.. code-block:: markdown
   :caption: Your Markdown page

   ---
   layout: "custom-layout"
   ---

   # Your Markdown page

   It uses the custom layout now.
