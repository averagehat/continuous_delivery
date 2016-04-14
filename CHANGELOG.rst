Changelog
=========

Version 1.0.4
-------------

- Added deploy_module script which installs tags from github and then builds
  environmental module for it

Version 1.0.3
-------------

- Added docs about protecting git branches

Version 1.0.2
-------------

- RTD and Travis badges and better description of project in README.md

Version 1.0.1
-------------

- Fixed the name in various places from continous to continuous

Version 1.0.0
-------------

- Stable release that is working

Version 0.0.6
-------------

- Unsilence most of release script except the last part
- No more tag.sh because it is really impossible to enforce what it was doing
- current_version.py now spits current project version from proj_dir/__init__.py's
  __version__

Version 0.0.5
-------------

- Silence the release push so github key not shown

Version 0.0.4
-------------

- Release has the v in front of it now

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
