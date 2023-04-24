.. meta::
   :description: Create functional and beautiful websites for your documentation with Sphinx and the Awesome Sphinx Theme.
   :keywords: Documentation, Sphinx, Python

Awesome Sphinx Theme
====================

.. rst-class:: lead

   Create functional and beautiful websites for your documentation with Sphinx.

----

Get started
-----------

#. Install the theme:

   .. .. code-block:: terminal

   ..    pip install sphinxawesome-theme

   .. literalinclude:: how-to/install/includes/install.sh
      :language: terminal

   .. seealso::

      .. button-ref:: how-to/install/index
         :ref-type: doc
         :color: primary
         :class: font-size-inherit

#. Add the theme to your Sphinx configuration:

   .. literalinclude:: how-to/add/includes/configure.inc
      :language: python
      :caption: File: conf.py

   .. seealso::

      .. button-ref:: how-to/add/index
         :ref-type: doc
         :color: primary
         :class: font-size-inherit

#. Build your documentation.

   .. seealso::

      .. button-link:: https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html
         :color: primary
         :class: font-size-inherit

         Get started with Sphinx

Learn more
----------


.. tab-set::

   .. tab-item:: How To

      In the **How-to** section, you can learn more about using and customizing the theme.

      .. toctree::
         :maxdepth: 1
         :caption: How To

         how-to/install/index
         how-to/add/index
         how-to/configure/index
         how-to/customize/index
         how-to/build-your-own/index

   .. tab-item:: Demo

      The **Demo** section shows how various elements will look like.

      .. toctree::
         :maxdepth: 1
         :caption: Demo
         :glob:

         demo/*
