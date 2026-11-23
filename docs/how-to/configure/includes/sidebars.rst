Sidebars
--------

The |product| uses the :confval:`sphinx:html_sidebars` setting for the sidebar.

The default setting is:

.. code-block:: python

   html_sidebars = {
     "**": ["sidebar_main_nav_links.html", "sidebar_toc.html"]
   }

This setting shows a sidebar on every page.
The sidebar contains the links to your documentation pages.
On small screens, it also contains the main navigation links from the header.

You can change the sidebar for each page.
For example, to hide the sidebar on large screens
but show the header navigation links on an ``about`` page:

.. code-block:: python

   html_sidebars = {
     "/about": ["sidebar_main_nav_links.html"]
   }

To hide the sidebar fully, use ``html_sidebars = {"**": []}``.
