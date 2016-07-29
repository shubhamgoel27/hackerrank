# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:18:37 2016

@author: Shubham

Karl has an array of  integers defined as . In one operation, he can delete any element from the array.

Karl wants all the elements of the array to be equal to one another. To do this, he must delete zero or more elements from the array. Find and print the minimum number of deletion operations Karl must perform so that all the array's elements are equal.

Input Format

The first line contains an integer, , denoting the number of elements in array . 
The next line contains  space-separated integers where element  corresponds to array element .
"""

from collections import Counter
#The length of array
n = input() 


arr = [int(x) for x in raw_input().split()]

    
def equalize_array(arr):
    count =  Counter(arr)
    if len(count) ==1:
        return 0
    most_common = count.most_common(1)
    
    return len(arr) - most_common[0][1]

print equalize_array(arr)