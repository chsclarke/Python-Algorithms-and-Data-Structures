# -*- coding: utf-8 -*-
"""
This is an example of Quick Sort in python 3.
wost case runtime theta(n^2)
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""

def partition(nums, low, high):

    pivot = nums[low]
    i = low
    j = high

    while True:
        while nums[j] >= pivot and j > low:
            j -= 1
        while nums[i] <= pivot  and i < high:
            i += 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            nums[low], nums[j] = nums[j], nums[low]
            return j
        

def QuickSort(nums, low, high):
    if (low < high):
        pivot = partition(nums, low, high)
        
        QuickSort(nums, low, pivot)
        QuickSort(nums, pivot + 1, high)


nums = [4,6,7,1,3,5,2,9,8,10,11,15,14,13,12]

QuickSort(nums, 0, len(nums) - 1)

print(nums)