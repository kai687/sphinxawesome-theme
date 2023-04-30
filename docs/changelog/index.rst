:orphan: true

Changelog
=========

.. rst-class:: lead

   This is the changelog of the |product|.

----

There will be a little bit more prose.

OLD
---

Updating the |product| is straightforward in most cases.
If you use any customization, you might have to update your
customizations manually.

Version 5.0
~~~~~~~~~~~

Version 5.0 of the |product| includes these **breaking changes**:

Remove support for ``html_collapsible_definitions``
   The user experience was bad for reference documentation,
   with users having to expand every object, only to see one comment line.
   Use the `sphinx-design <https://sphinx-design.readthedocs.io/en/latest/>`_ extension instead.
   The ``collapsible`` directive gives you more control.

No external link icons by default
   By default, no icons are shown.
   Set :ref:`opt:html_awesome_code_headers` to ``True`` to show icons for external links.
   In previous versions, external links always included an icon.


Version 4.0
~~~~~~~~~~~

Version 4.0 of the |product| includes these **breaking changes**:

Add support for Sphinx 6
   Since Sphinx 6 is only supported with the latest version of the `myst-parser` package
   and Sphinx 6 drops support for Python 3.7, this release is a major version update.

Apart from that, this version is identical with version 3 of the |product|.

Version 3.0
~~~~~~~~~~~

Redesign
   Create a better visual hierarchy which makes the document easier to scan.
   Heavily inspired by the `Material Design <https://m2.material.io/>`_ website.

Restructure
   All JavaScript is now using the `Stimulus <https://stimulus.hotwired.dev/>`_ framework.

Version 2.0
~~~~~~~~~~~

Version 2.0 of the |product| includes these **breaking changes**:

Require Sphinx 4 or newer
   Sphinx 4 depends on docutils 0.17, which creates more semantic HTML by default.
   This allows to reduce the amount of custom transformations.

Restructure several templates
   The layout use `CSS grid <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout>`_.
   This leads to fewer container elements in the templates.
