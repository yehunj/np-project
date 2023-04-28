#!/bin/bash

PYTHON=/usr/bin/python
SCRIPT=TSP.py

for FILENAME in test_cases/*.txt; do
    echo "Running test case $FILENAME"
    $PYTHON $SCRIPT < $FILENAME
done