# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 12:01:33 2016

@author: Shubham
"""

def subway_hacker( arr1, arr2):
    #sum = 0
    equals = [0]
    length = len(arr1)
    if len(arr2) < len(arr1):
        length = len(arr2)
        
    #Store all positions at which coins are equal i.e. track can be switched    
    for i in range(length):
        if arr1[i] == arr2[i]:
            equals.append(i)
    #Calculate the sums of different portions, partitioned when the track can be switched        
    portions_1 = []
    portions_2 = []
    for i in range(len(equals)-1):
        temp_1 = arr1[equals[0]:equals[i+1]+1]
        #print temp_1
        portions_1.append(sum(temp_1))
        #print portions_1
        portions_2.append(sum(arr2[equals[0]:equals[i+1]+1]))
        #print portions_2
    portions_1.append(sum(arr1[equals[-1]+1:]))
    portions_2.append(sum(arr2[equals[-1]+1:]))
    #print portions_1
    #print portions_2
    
    total = []
    for i in range(len(portions_1)):
        if portions_1[i] > portions_2[i]:
            total.append(portions_1[i])
        else:
            total.append(portions_2[i])
    #aaaand your legendary status is maintained
    return sum(total)
        
        
        
        
    
a = [9, 15, 21, 27, 60, 75, 91, 102]
b = [3, 12, 21, 33, 42, 75, 205]
print subway_hacker( a,b)     

a = [10,20,30]
b = [1,20,9]

print subway_hacker(a,b)   