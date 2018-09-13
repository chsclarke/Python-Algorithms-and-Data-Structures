def findElement(key, lst, low, high):

    mid = (high + low - 1) // 2
    
    if (high <= low):
        return -1

    if lst[mid] == key: 
        return mid

    if key < lst[mid]:
        return findElement(key, lst, low, mid-1)

    if key > lst[mid]:
        return findElement(key, lst, mid+1, high)

lst = [1,2,3,4,5,6,7,8]
print(findElement(8, lst, 0, len(lst)))
