#!/bin/bash

PYTHON=/usr/bin/python
SCRIPT=TSP.py

# Loop through all the test case files in the test_cases directory
for FILENAME in test_cases/*.txt; do
    # Run the script with the test case file as input
    echo "Running test case $FILENAME"
    $PYTHON $SCRIPT < $FILENAME
done