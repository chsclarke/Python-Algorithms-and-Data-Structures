# -*- coding: utf-8 -*-
"""
This is an example of insertion sort in python 3.
wost case runtime O(n^2)
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""

def InsertionSort(input):
    input_size = len(input)
    sorted = input
    j = 0
    temp = 0
    
    #input size iterations
    for i in range(1, input_size):
        temp = sorted[i]
        j = i-1
        
        #iterate backwards in list, pushing elements until correct spot found.
        #using temp variable because the list is changing between iterations of first loop
        while(j >= 0 and temp < sorted[j]):
            sorted[j+1] = sorted[j]
            j -= 1
        
        #inserting at that location input[j+1]
        sorted[j+1] = temp

    return sorted


input = [2,8,1,6,7,15,12]

print(InsertionSort(input))

