#!/bin/bash

# Path to your requirements.txt file
requirements_file="requirements.txt"

# Read each line in requirements.txt
while read package || [[ -n $package ]];
do
    echo "Attempting to install $package using conda..."
    conda install --yes $package || {
        echo "Failed to install $package with conda. Attempting with pip..."
        pip install $package
    }
done < $requirements_file
