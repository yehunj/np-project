#!/bin/bash

PYTHON=/usr/bin/python
SCRIPT=cs412_tsp_approx.py

for FILENAME in test_cases/*.txt; do
    echo "Running test case $FILENAME"
    python $SCRIPT < $FILENAME
done