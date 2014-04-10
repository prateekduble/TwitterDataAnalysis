#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    tokens = line.split(',')
    if len(tokens) >= 3:
        w = tokens[2].replace("\"", " ")
        words = w.split()
        # increase counters
        for word in words:
            print '%s\t%s' % (word, 1)
