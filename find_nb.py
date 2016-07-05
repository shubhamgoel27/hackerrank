# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 01:00:39 2015

@author: Shubham
"""

"""You are given the total volume m of the building. 
Being given m can you find the number n of cubes you will have to build?

The parameter of the function find_nb() will be an integer m and you have to return the integer n
 such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Sum of first n cubes, m = (n^2*(n+1)^2)/4
"""

from math import sqrt

def find_nb(m):
    rhs = 2.0* sqrt(m)
    D = sqrt(1.0 + 4*rhs)
    n = (-1.0 + D)/2.0
    return int(n) if n.is_integer() else -1
    
    