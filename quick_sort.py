# -*- coding: utf-8 -*-
"""
This is an example of quick sort in python 3.
runtime O(nLgn), O(n^2) worst case
This implimentation of quick sort chooses a random pivot and recursivly sorts on a linked list.
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""
import random

def partition(input, left, right):
    pivot = input[(left + right)//2]
    
    while(left <= right):
        while (input[left] < pivot):
            left += 1
            print("left",left, "right", right)
        while (input[right] > pivot):
            right -= 1
            print("left",left, "right", right)
        if (left <= right):
            print("swap")
            input[right], input[left] = input[left], input[right]
            print(input)
            left+= 1
            right-= 1

    return left

def QuickSort(input, left, right):
    if (left <= right):
        index = partition(input, left, right)

        QuickSort(input, left, index-1)
        QuickSort(input, index+1, right)
    else:
        return

#MAIN:

input = [2,8,1,6,7,4,3,5]

QuickSort(input,0,len(input)-1)

print(input)











