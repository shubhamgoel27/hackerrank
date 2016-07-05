# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:31:44 2016

@author: Shubham

PROBLEM STATEMENT:

James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can reduce the value of a letter, e.g. he can change d to c, but he cannot change
 c to d.
In order to form a palindrome, if he has to repeatedly reduce the value of a letter,
 he can do it until the letter becomes a. Once a letter has been changed to a,
 it can no longer be changed.
Each reduction in the value of any letter is counted as a single operation.
 Find the minimum number of operations required to convert a given string into a 
 palindrome.
"""

string = 'cba'

def convert_palindrome(string):
    total_count = 0
    length = len(string)
    
    for i in range(length/2):
        if string[i] != string[length-i-1]:
            diff = abs(ord(string[i]) - ord(string[length-i-1]))
            total_count += diff
            #print string[i], '---',diff, '---', string[length-i-1]
    #print 'Total changes to be made: ', total_count
    return total_count
            
n = input()
data = []
output = []
for i in range(n):
    inp = raw_input()
    data.append(inp)
    output.append(convert_palindrome(inp))
    
for i in range(n):
    print output[i]
    
