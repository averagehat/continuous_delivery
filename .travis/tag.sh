#!/bin/bash

if [ -z "${TRAVIS_TAG}" ]
then
    echo "Not a tag. Skipping"
    exit 0
fi

set -e

# Make sure version is changed
git diff $(basename $TRAVIS_REPO_SLUG)/__init__.py | grep -q '^.__version__'
