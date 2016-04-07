.. continous delivery documentation master file, created by
   sphinx-quickstart on Fri Mar 27 15:46:28 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to continuous_delivery's documentation!
===============================================

The goal of this project is just to get a simple continous delivery(deployment?)
setup working between TravisCI and GitHub.

Since Travis gives you a few variables:

- TRAVIS_REPO_SLUG(necrolyte2/continous_delivery)
- TRAVIS_BRANCH(master, develop or anything else)
- TRAVIS_PULL_REQUEST(false or PR number)
- TRAVIS_TAG(tag or empty)

We can enforce the following:
-----------------------------

- If TRAVIS_BRANCH is master
  - Ensure CHANGELOG.rst has changed
- If TRAVIS_BRANCH is develop
  - Ensure CHANGELOG.rst and docs/ has changed
- If TRAVIS_BRANCH is master and TRAVIS_PULL_REQUEST is false and __version__ has changed
  - Push a new tag to github(essentially an unannotated release)

What this enforces:
-------------------

- You do new features in branches off of develop
  - Each PR from feature to develop requres changelog and docs be updated to ensure
    develop stays well documented with what changes happened
- Any time anything has PR against master, the changelog is checked to make sure it
  was updated again since hotfixes go directly to master skipping develop
- Whenever the __version__ is updated and gets merged into master, a new tag
  will be automatically pushed to the project.

Setup
-----

1. Head over to https://github.com/settings/tokens and generate a new token
   Until a better way is found, we will use Personal Access Tokens
2. Head over to your project's travis page(https://travis-ci.org/user/project/settings)
   and add a new variable GH_TOKEN and the value will be your Github personal access
   token
3. Copy the .travis directory from this project into your project
4. Modify your .travis.yml to contain all of the before_script and after_success
   from this .travis.yml

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

