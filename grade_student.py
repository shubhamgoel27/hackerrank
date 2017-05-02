#!/bin/python

import sys

def solve(grades):
	res = []
	for grade in grades:
		if grade>=38:
			if grade%5>2:
				grade = grade + (5 - grade%5)
		res.append(grade)
	return res


n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
	grades_t = int(raw_input().strip())
	grades.append(grades_t)
result = solve(grades)
print " ".join(map(str, result))

