Add custom templates
~~~~~~~~~~~~~~~~~~~~

You can define custom layouts and templates for your pages.

For example, to make your own footer template,
make a file :file:`_templates/footer.html` with this content:

.. code-block:: html+jinja
   :caption: File: _templates/footer.html

   {# A custom footer template that does not inherit from the parent. #}

   <div style="background-color: red;">
      Your custom footer.
   </div>

.. seealso::

   :ref:`sec:add-custom-templates`
