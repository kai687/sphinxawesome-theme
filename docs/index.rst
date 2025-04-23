.. meta::
   :description: Create functional and beautiful websites for your documentation with Sphinx and the Awesome Sphinx Theme.
   :twitter:description: Create functional and beautiful websites for your documentation with Sphinx and the Awesome Sphinx Theme.

Awesome Sphinx Theme
====================

.. rst-class:: lead

   Create functional and beautiful websites for your documentation with Sphinx.

----

This is the documentation for version |current| of the |product|.

Get started
-----------

#. Install the theme:

   .. literalinclude:: how-to/install/includes/install.sh
      :language: sh

   .. seealso::

      :doc:`how-to/install/index`

#. Add the theme to your Sphinx configuration:

   .. literalinclude:: how-to/add/includes/configure.inc
      :language: python
      :caption: |conf|

   .. seealso::

      :doc:`how-to/add/index`,
      :doc:`how-to/configure/index`

#. Build your documentation.

   .. seealso::

      `Get started with Sphinx <https://docs.readthedocs.com/platform/stable/intro/sphinx.html>`_

Upgrade
-------

If you want to upgrade to version |current| of the theme, see :doc:`changelog/index`.

Explore
-------

.. tab-set::

   .. tab-item:: How To

      In the **How-to** section, you can learn more about using and customizing the theme.

      .. toctree::
         :caption: How To
         :titlesonly:

         how-to/install/index
         how-to/add/index
         how-to/configure/index
         how-to/customize/index
         how-to/build-your-own/index

   .. tab-item:: Demo

      The **Demo** section shows how various elements will look like.

      .. toctree::
         :caption: Demo
         :glob:
         :titlesonly:

         demo/*

.. toctree::
   :hidden:
   :caption: API demo

   autoapi/api/index
