Add custom JavaScript
=====================

To add custom JavaScript,
you can add JavaScript files
or extend templates to add your code inline.

Add JavaScript files
--------------------

To add extra JavaScript files, add your code to a file—for example,
:file:`_static/custom.js` and add the following options to your Sphinx configuration:

.. code-block:: python
   :caption: File: conf.py

   html_static_path = ["_static"]
   html_js_files = ["custom.js"]

.. seealso::

   :confval:`sphinx:html_static_path`
   :confval:`sphinx:html_js_files`

Extend templates with inline JavaScript
---------------------------------------

If you want to add JavaScript inline,
or load additional external scripts,
you can extend the default ``page`` template
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
