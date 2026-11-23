Logos
-----

Set the path to your logo with the :confval:`sphinx:html_logo` option.
If your logo works well in dark mode, you need only one logo.

To use different logos for *light* and *dark* mode,
add them to your theme options:

.. code-block:: python
   :caption: |conf|

   html_theme_options = {
       "logo_light": "path/to/light/logo",
       "logo_dark": "path/to/dark/logo"
   }
