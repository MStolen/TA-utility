#!/bin/sh

# Run pre-lab check on files with default parameters
# Go to directory above this one
cd "$(dirname "$0")"/..

source ./venv/bin/activate # Enter virtual environment
python -m ta_utility check-pre-labs # Run command
deactivate # Exit virtual environment
