#!/bin/bash

if [ "${TRAVIS_BRANCH}" != "master" ]
then
    exit 0
fi

set -e

# Make sure changelog is updated
.travis/in_commit.sh CHANGELOG.rst
