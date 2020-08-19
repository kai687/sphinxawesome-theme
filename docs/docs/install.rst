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

If you want to try the latest features,
install the theme directly from Github:

.. code-block:: console

   $ pip install git+https://github.com/kai687/sphinxawesome-theme.git

Check the "MASTER" section in the CHANGELOG_ file.
These features are available in the development version,
but not yet in the released version.

.. _CHANGELOG: https://github.com/kai687/sphinxawesome-theme/blob/master/CHANGELOG.rst

Installing the theme locally
----------------------------

If you want to modify the theme,
`fork the repository`_ [#]_
and clone it into a directory accessible to your Sphinx project,
for example :dir:`./_themes`.

.. _fork the repository: https://help.github.com/en/github/getting-started-with-github/fork-a-repo

.. samp::

   $ cd _themes/
   $ git clone https://github.com/{YOUR_GITHUB_USERNAME}/sphinxawesome-theme.git

Replace :samp:`{YOUR_GITHUB_USERNAME}` with your Github user name.

.. seealso::

   - :ref:`How to use a local version of the theme`
   - :ref:`How to modify the theme`

.. [#] You only need to fork the repository if you want to merge your modifications with
       the main repository.
