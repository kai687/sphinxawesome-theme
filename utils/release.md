# Release a new version

This page documents the steps to releasing a new version.

## Update the version string

First, update the version string for the Python project and create a new PR.

```bash
NEW_VERSION="3.3.0"
OLD_VERSION="$(poetry version -s)"
```

1. Create a new branch:

   ```bash
   git checkout master
   git pull
   git checkout -B chore/new-release
   ```

2. Update the version of the Python project:

   ```bash
   poetry version ${NEW_VERSION}
   ```

3. Update the version of the JavaScript project:

   ```bash
   cd src/theme-src
   yarn version --new-version ${NEW_VERSION}
   ```

4. Update the version string in a test file:

   ```bash
   cd ~theme
   sed "s/${OLD_VERSION}/${NEW_VERSION}/" ../tests/test_sphinxawesome_theme.py > tmp
   mv tmp ../tests/test_sphinxawesome_theme.py
   ```

5. Update the version string in the `CHANGELOG` file:

   ```bash
   sed "s/HEAD/${NEW_VERSION}/" ../CHANGELOG.rst > tmp
   mv tmp ../CHANGELOG.rst
   ```

6. Commit the change:

   ```bash
   git commit --all --message "chore: version update"
   git push origin
   PR_URL=$(gh pr create --fill --assignee "kai687" --label "maintenance")
   ```

7. Merge the PR after CI completed and open the PR on GitHub:

   ```bash
   gh pr merge "${PR_URL}" --auto
   gh pr view --web
   ```

8. After merging the PR, tag a new release:

   ```bash
   git checkout master
   git pull
   git tag ${NEW_VERSION}
   git push origin ${NEW_VERSION}
   ```
