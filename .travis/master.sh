#!/bin/bash

set -e

# Make sure changelog is updated
.travis/in_commit.sh CHANGELOG.rst
