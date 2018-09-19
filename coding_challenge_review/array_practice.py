
def mergeSorted(arr1, arr2):
    #code to merge two sorted arrays
    sortedArr = [None] * (len(arr1) + len(arr2))
    i = 0
    j = 0
    k = 0

    #iterate through both list and insert the lower of the two
    while(i < len(arr1) and j < len(arr2)):
        # <= allows function to support duplicate values
        if (arr1[i] <= arr2[j]):
            sortedArr[k] = arr1[i]
            i += 1
            k += 1

        else:
            sortedArr[k] = arr2[j]
            j += 1
            k += 1

    #merge the leftovers of the larger list
    while i < len(arr1):
        sortedArr[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        sortedArr[k] = arr2[j]
        j += 1
        k += 1

    return sortedArr


if __name__ == '__main__':

    arr1 = [1,3,5,7,9]
    arr2 = [2,4,6,7,7,8,10,12,13,14]

    print(mergeSorted(arr1,arr2))






        
