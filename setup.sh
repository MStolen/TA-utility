#!/bin/sh
# Run this script in this folder to create the default folder structure
# and install the required packages

# Make sure location is the root folder of the project
cd "$(dirname "$0")"
# Create default directory structure
mkdir output section_lists pre_lab_lists
# Create virtual environment and install required packages
python3 -m venv ./venv/
source ./venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
deactivate

