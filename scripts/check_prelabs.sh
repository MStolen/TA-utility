#!/bin/sh

# Run pre-lab check on files with default parameters
# Change the next line in order to be able to run script from any directory
# by adding an absolute path to the root folder
cd ..
# shellcheck disable=SC2039
source ./venv/bin/activate
python -m ta_utility check-pre-labs
deactivate
