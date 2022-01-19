#!/bin/sh

# Run make-sign-ins check on files with default parameters
# Go to directory above this one
cd "$(dirname "$0")"/..
source ./venv/bin/activate # Enter virtual environment
python -m ta_utility sign-in # Run command
deactivate # Exit virtual environment