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
