#!/bin/sh

# Run pre-lab check on files with default parameters
# Change and uncomment next line in order to be able to run script from any directory
# cd 3201_Utility/
source ./venv/bin/activate
python -m 3201_utility check-pre-labs
deactivate
