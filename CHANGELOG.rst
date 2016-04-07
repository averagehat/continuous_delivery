Changelog
=========

Version 0.0.3
-------------

- Releases new tag to github automatically when branch is master and 
  $(basename $TRAVIS_REPO_SLUG)/__init__.py's __version__ is updated

Version 0.0.2
-------------

- Ensures version update when new tag is pushed/merged
- Fixed project directory name

Version 0.0.1
-------------

- Implemented check for changelog and docs for master and develop
