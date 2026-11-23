.. meta::
   :description: Add JavaScript files or add code inline by extending the templates.
   :twitter:description: Add JavaScript files or add code inline by extending the templates.

Add custom JavaScript
=====================

.. rst-class:: lead

   Add JavaScript files or add code inline by extending the templates.

Add JavaScript files
--------------------

To add extra JavaScript files, put your code in a file, for example :file:`_static/custom.js`.
Then add these options to your Sphinx configuration:

.. code-block:: python
   :caption: |conf|

   html_static_path = ["_static"]
   html_js_files = ["custom.js"]

.. seealso::

   :confval:`sphinx:html_static_path`
   :confval:`sphinx:html_js_files`

Extend templates with inline JavaScript
---------------------------------------

To add JavaScript inline,
or to load more external scripts,
extend the default ``page`` template
and override the ``extrahead`` block:

.. code-block:: html+jinja
   :caption: File: page.html

   {% extends "!page.html" %}

   {{ super() }}

   {% block extrahead %}
   <script>
    // Add your JavaScript code here
   </script>
   {% endblock %}
