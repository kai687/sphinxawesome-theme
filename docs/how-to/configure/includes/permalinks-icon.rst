Permalinks icons
----------------

By default, Sphinx adds a link to each heading which allows you to link to each section of a page.
Sphinx adds a ¶ icon by default.

Even if you want to use the default icon, it's better to wrap it in a ``<span>`` element:

.. code-block:: python
   :caption: |conf|

   html_permalinks_icon = "<span>¶</span>"

This makes the icon only show up when you hover over or focus the heading.

If you want to use the same icon as used in the documentation for the |product|,
add the following code to your Sphinx configuration:

.. code-block:: python
   :caption: |conf|

   from sphinxawesome_theme.postprocess import Icons

   html_permalinks_icon = Icons.permalinks_icon
