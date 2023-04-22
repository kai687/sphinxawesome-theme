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

You can create custom layouts and choose different page layouts for different pages.

To create a custom layout, create a new file :file:`_templates/custom-layout.html`:

.. code-block:: html+jinja
   :caption: File: _templates/custom-layout.html

   <html>
      <body>{{ body }}</body>
   </html>

Then, select the layout in your document with the ``layout`` option.

.. tab-set-code::

   .. code-block:: markdown
      :class: no-header

      ---
      layout: "custom-layout"
      ---

   .. code-block:: rst
      :class: no-header

      :layout: custom-layout
