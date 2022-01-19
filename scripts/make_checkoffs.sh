#!/bin/sh

# Run make-checkoffs check on files with default parameters. Required input argument is the checkoff header

# Go to directory above this one
cd "$(dirname "$0")"/..
source ./venv/bin/activate # Enter virtual environment
python -m ta_utility make-checkoffs -ch "$1" # Run command
deactivate # Exit virtual environment