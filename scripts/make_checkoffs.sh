#!/bin/sh

# Run make-checkoffs check on files with default parameters. Required input argument is the checkoff header
# Change the next line in order to be able to run script from any directory
# by adding an absolute path to the root folder
cd ..
# shellcheck disable=SC2039
source ./venv/bin/activate
python -m ta_utility make-checkoffs -ch "$1"
deactivate