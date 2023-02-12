#!/usr/bin/env bash

find . -type f -name .DS_Store -exec rm -f {} \;
rm -rf ./dist
rm -rf ./slim_helper.egg-info

python setup.py sdist
twine upload dist/*
