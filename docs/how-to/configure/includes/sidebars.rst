Sidebars
--------

The |product| uses the :confval:`sphinx:html_sidebars` setting to configure the sidebar.

The default setting is:

.. code-block:: python

   html_sidebars = {
     "**": ["sidebar_main_nav_links.html", "sidebar_toc.html"]
   }

This includes a sidebar on every page.
The sidebar includes the main navigation links (from the header) on small screens,
and the links to your documentation pages.

You can change the sidebar for individual pages.
For example, to hide the sidebar on large screens,
but still show the header navigation links on an ``about`` page:

.. code-block:: python

   html_sidebars = {
     "/about": ["sidebar_main_nav_links.html"]
   }

To hide the sidebar completely, use ``html_sidebars = {"**": []}``.
