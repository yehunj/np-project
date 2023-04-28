#!/bin/bash

PYTHON=/usr/bin/python
SCRIPT=cs412_tsp.py

for FILENAME in test_cases/*.txt; do
    echo "Running test case $FILENAME"
    $PYTHON $SCRIPT < $FILENAME
done