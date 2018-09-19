import math

def print2Smallest(arr):
 
    # There should be atleast two elements
    arr_size = len(arr)
    if arr_size < 2:
        print ("Invalid Input")
        return
 
    first = second = float("inf")
    for i in range(0, arr_size):
 
        # If current element is smaller than first then
        # update both first and second
        if arr[i] < first:
            second = first
            first = arr[i]
 
        # If arr[i] is in between first and second then
        # update second
        elif (arr[i] < second and arr[i] != first):
            second = arr[i]
 
    if (second == float("inf")):
        print ("No second smallest element")
    else:
        print ('The smallest element is',first,'\nSecond smallest element is',second )
 

if __name__ == '__main__':
    arr = [1,3,2,5,4,7,9]
    print2Smallest(arr)