Permalinks icons
----------------

By default, Sphinx adds a link with a ¶ icon to each heading.
You can use these links to link to each section of a page.

To use the default icon, put it in a ``<span>`` element:

.. code-block:: python
   :caption: |conf|

   html_permalinks_icon = "<span>¶</span>"

With this change, the icon shows only when you hover over the heading or move focus to it.

To use the same icon as the documentation for the |product|,
add this code to your Sphinx configuration:

.. code-block:: python
   :caption: |conf|

   from sphinxawesome_theme.postprocess import Icons

   html_permalinks_icon = Icons.permalinks_icon
