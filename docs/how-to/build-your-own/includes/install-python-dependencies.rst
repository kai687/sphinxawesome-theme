Install the Python dependencies
-------------------------------

#. :ref:`sec:fork-and-clone`.

#. Install the Python dependencies:

   .. code-block:: terminal

      poetry install

#. Optional: install and test the pre-commit hooks:

   .. code-block:: terminal

      poetry run pre-commit install

   If you don't plan on committing any changes to the repository,
   you can skip this step.
   You can see the active pre-commit hooks in the file :gh:`.pre-commit-config.yaml`.

   To test pre-commit with Poetry, run:

   .. code-block:: terminal

      poetry run pre-commit run --all

#. Test your Nox environment.

   You can run any Nox session to confirm that the environment is working.
   To list the available sessions, run:

   .. code-block:: terminal

      nox --list-sessions

   For example, run all default sessions:

   .. code-block:: terminal

      nox
