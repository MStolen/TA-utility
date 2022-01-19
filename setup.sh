#!/bin/sh
# Run this script in this folder to create the default folder structure
# and install the required packages
mkdir output section_lists pre_lab_lists
python3 -m venv ./venv/
source ./venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
deactivate

