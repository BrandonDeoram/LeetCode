def replaceElements(arr):
    rightMax = -1
    for i in range(len(arr)-1,-1,-1):
        newMax = max(arr[i],rightMax)
        print(newMax)
        arr[i] = rightMax
        rightMax = newMax
       
    return arr


print(replaceElements([17, 18, 5, 4, 6, 1]))
