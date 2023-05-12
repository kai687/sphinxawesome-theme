Logos
-----

You can use the :confval:`sphinx:html_logo` option to set a path to your logo.
If you're using a logo that works well in dark mode, you only need to declare one logo.

If you want to use different logos for *light* and *dark* mode,
add them to your theme options:

.. code-block:: python
   :caption: |conf|

   html_theme_options = {
       "logo_light": "path/to/light/logo",
       "logo_dark": "path/to/dark/logo"
   }
