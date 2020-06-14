How to install the theme
========================

Installing a release version (recommended)
------------------------------------------

If you want to install a released version from PyPI_,
follow these instructions.

.. include:: ../../README.rst
   :start-after: install-start
   :end-before: install-end

.. _PyPI: https://pypi.org/

Installing a development version
--------------------------------

Releases are planned often,
so it shouldn't be needed for most users,
but you can install the theme directly from Github:

.. code-block:: console

   $ pip install git+https://github.com/kai687/sphinxawesome-theme.git

Creating a local copy of the theme
----------------------------------

If you want to modify the theme,
`fork the repository
<https://help.github.com/en/github/getting-started-with-github/fork-a-repo>`_
and clone it into a directory accessible to your Sphinx project,
for example :dir:`./_themes`.

.. samp::

   $ git clone https://github.com/{YOUR_GITHUB_USERNAME}/sphinxawesome-theme.git

To use a local copy of the theme, follow the steps described in
:ref:`Using a local version of the theme`.

To change the theme,
follow the steps in :ref:`How to modify the theme`.

.. note::

   If you only want to create a local copy, forking the repository first is not
   necessary.
