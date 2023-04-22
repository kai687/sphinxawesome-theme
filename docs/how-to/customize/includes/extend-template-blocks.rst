Extend template blocks
~~~~~~~~~~~~~~~~~~~~~~

To add code, you can :ref:`extend the page template <sec:extend-templates>` and override the template blocks:

``extrahead``
   Adds your template code before the closing ``</head>`` tag.
   This is useful to add custom styles or JavaScript code.

``extrabody``
   Adds extra code **after** the main content, before the footer.

.. code-block:: html+jinja
   :caption: File: page.html

   {% extends "!page.html" %}

   {{ super() }}

   {% block extrahead %}
   {# Included before the closing </head> tag #}
   {% endblock %}

   {% block extrabody %}
   {# Included after the main content, before the <footer> #}
   {% endblock %}
