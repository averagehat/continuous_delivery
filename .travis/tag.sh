#!/bin/bash

if [ -z "${TRAVIS_TAG}" ]
then
    echo "Not a tag. Skipping"
    exit 0
fi

set -e
# Ensure version changed
.travis/version_updated.sh
