Extend template blocks
~~~~~~~~~~~~~~~~~~~~~~

To add code, :ref:`extend the page template <sec:extend-templates>`. Then override these template blocks:

``extrahead``
   Adds your template code before the closing ``</head>`` tag.
   Use this block to add custom styles or JavaScript code.

``body_before``
   Adds content to the top of the page.

``body_after``
   Adds content to the bottom of the page.

``header``
   Replaces the header of the page.

``sidebar``
   Replaces the left sidebar.

``main``
   Replaces the ``<main>`` element that contains the body and the on-page table of contents.

``footer``
   Replaces the footer of the page.

``scripts``
   Replaces the JavaScript ``<script>`` tags at the end of the page.
   Call ``{{ super() }}`` in this block to keep the default scripts.

To change parts of the header, :ref:`extend the header template <sec:extend-templates>`
and override these blocks:

``header_before``
   Adds content at the top of the header.

``header_after``
   Adds content at the bottom of the header.

``header_left``
   Replaces the left side of the header, which contains the logo and the main navigation links.

``header_logo``
   Replaces the logo and the title of the documentation.

``header_main_nav``
   Replaces the main navigation links.

``mobile_menu``
   Replaces the button that opens the sidebar on small screens.

``header_right``
   Replaces the right side of the header, which contains the search box, the extra link icons, and the theme switcher.

``extra_header_link_icons``
   Replaces the extra link icons and the theme switcher.

``theme_switcher``
   Replaces the button that switches between light mode and dark mode.

.. code-block:: html+jinja
   :caption: File: page.html

   {% extends "!page.html" %}

   {{ super() }}

   {% block extrahead %}
   {# Included before the closing </head> tag #}
   {% endblock %}

   {% block body_before %}
   {# Included at the top of the page #}
   {% endblock %}

   {% block body_after %}
   {# Included at the bottom of the page #}
   {% endblock %}
