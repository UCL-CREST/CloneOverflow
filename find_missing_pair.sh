#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    cat fragments_nicad_fse13_160813.xml | grep $line	
done < "$1"
