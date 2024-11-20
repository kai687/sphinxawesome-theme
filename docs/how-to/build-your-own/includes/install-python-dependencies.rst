Install the Python dependencies
-------------------------------

#. :ref:`sec:fork-and-clone`.

#. Install the Python dependencies:

   .. code-block:: bash

      uv sync

#. Optional: install and test the pre-commit hooks:

   .. code-block:: bash

      uv tool install pre-commit
      pre-commit install --hook-type pre-push

   If you don't plan on publishing any changes to the repository,
   you can skip this step.
   You can see the active pre-commit hooks in the file :gh:`.pre-commit-config.yaml`.

   To test hooks, run:

   .. code-block:: bash

      pre-commit run --all

   .. note::

      This project runs the hooks before you push instead.
      More commonly, hooks run before every commit.

#. Test your Nox environment.

   You can run any Nox session to confirm that the environment is working.
   To list the available sessions, run:

   .. code-block:: bash

      nox --list-sessions

   For example, run all default sessions:

   .. code-block:: bash

      nox
