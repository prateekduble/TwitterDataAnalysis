#!/bin/sh
# 
# Usage: extractCoordinates.sh tweets.csv coordinates.csv
#
file=$1
cat $file | grep -o 'coordinates.*\]' | sed 's/.*\[\(\-*[0-9]*\.[0-9]*\)\,\ \(\-*[0-9]*\.[0-9]*\)\].*/\1\,\2/' > $2
