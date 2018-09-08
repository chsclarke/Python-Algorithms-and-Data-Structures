# -*- coding: utf-8 -*-
"""
This is an example of selection sort in python 3.
wost case runtime O(n^2)
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""
import struct

def SelectionSort(input):
    unsorted = input
    input_size = len(input)
    sorted = []
    
    #input size iterations
    for i in range(0,input_size):
        
        #max int size
        min = platform_c_maxint = 2 ** (struct.Struct('i').size * 8 - 1) - 1
        
        #finding smallest variable in unsorted array
        for j in range(0, len(unsorted)):
            if (unsorted[j] < min):
                min = unsorted[j]
    
        #taking element from unsorted and inserting in sorted
        unsorted.remove(min)
        sorted.append(min)

    return sorted




input = [2,8,1,6,7,15,12]


print(SelectionSort(input))
