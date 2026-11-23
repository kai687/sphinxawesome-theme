.. _sec:fork-and-clone:

Create a local copy of the repository
-------------------------------------

#. Optional: `fork the repository`_ .

   If you do not want to merge your changes into the original repository,
   skip this step.

#. `Clone the repository`_:

   - If you forked the repository, run:

     .. code-block:: bash
        :emphasize-text: GITHUB_USERNAME

        git clone https://github.com/GITHUB_USERNAME/sphinxawesome-theme.git

     Replace :samp:`{GITHUB_USERNAME}` with your GitHub username.

   - If you did not fork the repository, clone the original repository:

     .. code-block:: bash

        git clone https://github.com/kai687/sphinxawesome-theme.git

.. _`fork the repository`: https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo
.. _`Clone the repository`: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

After you clone the repository,
you can :ref:`install the theme as a local package<sec:install-local-package>`
or :doc:`install the dependencies of the project <../build-your-own/index>`.
