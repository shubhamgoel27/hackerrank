#!/bin/python

import sys


n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(unsorted_t)

unsorted.sort(key = int)
for val in unsorted:
    print val