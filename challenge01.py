#!/usr/bin/python

import sys

filename = sys.argv[1]
lines = open(filename, 'r').readlines()
lines.pop(0)


for line in lines:
    print((int(line) + 1) / 2)
