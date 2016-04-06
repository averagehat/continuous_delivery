#!/bin/bash

if [ "${TRAVIS_BRANCH}" != "develop" ]
then
    exit 0
fi

set -e

./travis/in_commit.sh CHANGELOG.rst docs/
