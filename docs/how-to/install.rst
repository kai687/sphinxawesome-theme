.. meta::
   :description: Learn how to install the Awesome Theme for your documentation project.

Install the theme
=================

.. rst-class:: lead

   Install the |product| as a Python package or copy it into a local directory.

.. contents:: On this page
   :local:
   :backlinks: none

.. _sec:install-python-package:

Install as a Python package
---------------------------

Install the latest **released version** from the Python Package Index
`PyPI <https://pypi.org/project/sphinxawesome-theme/>`_:

.. code-block:: terminal

   pip install sphinxawesome-theme

To install the latest **development version**, run:

.. code-block:: terminal

   pip install git+https://github.com/kai687/sphinxawesome-theme.git


See the :gh:`CHANGELOG <CHANGELOG.md>` file for extra features and updates in the
development version that aren't released yet.


After installing the theme, you can :doc:`add it to your project <add>`.

.. _sec:install-local-package:

Install from a local directory
------------------------------

If you want to build your own version of the theme,
you can clone the repository and install the cloned version
as a `local Python package <https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-a-local-src-tree>`_.

#. :ref:`sec:fork-and-clone`.
#. Install the local copy of the theme in your project:

   .. code-block:: terminal
      :emphasize-text: /path/to/sphinxawesome_theme

      pip install --editable /path/to/sphinxawesome_theme

   Replace :samp:`{/path/to/sphinxawesome_theme}` with the path to your local copy
   of the theme.
   The ``--editable`` option installs the package in editable, or development, mode.

After installing the theme, you can :doc:`add it to your project <add>`.

.. _sec:fork-and-clone:

Create a local copy of the repository
-------------------------------------

#. Optional: `fork the repository`_ .

   If you don't want to merge your changes with the original repository,
   you can skip this step.

#. `Clone the repository`_:

   - If you forked the repository, run:

     .. code-block:: terminal
        :emphasize-text: GITHUB_USERNAME

        git clone https://github.com/GITHUB_USERNAME/sphinxawesome-theme.git

     Replace :samp:`{GITHUB_USERNAME}` with your GitHub username.

   - If you didn't fork the repository, clone the original repository:

     .. code-block:: terminal

        git clone https://github.com/kai687/sphinxawesome-theme.git

.. _`fork the repository`: https://docs.github.com/en/get-started/quickstart/fork-a-repo
.. _`Clone the repository`: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

After cloning the repository,
you can :ref:`install the theme as a local package<sec:install-local-package>`
or :doc:`install the project's dependencies <build-your-own>`.
