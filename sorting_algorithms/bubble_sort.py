# -*- coding: utf-8 -*-
"""
This is an example of bubble sort in python 3.
wost case runtime O(n^2)
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""

def BubbleSort(input):
    input_size = len(input)
    sorted = input
    
    #input size iterations
    for i in range(0, input_size):
        
        #only need to check up to input_size-i-1 because rest is sorted
        for j in range(0, input_size-i-1):
            
            if (sorted[j] > sorted[j+1]):
                
                #python shorthand for swapping values
                sorted[j], sorted[j+1] = sorted[j+1], sorted[j]

    return sorted


input = [2,8,1,6,7,15,12]

print(BubbleSort(input))
