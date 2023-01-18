

def containsDuplicate(nums):
    #Empty map 
    prevMap = {}
    #Loop through array , adding +1 to each number we seen into the map 
    for n in enumerate(nums):
        if(n[1] in prevMap):
            return True
        prevMap[n[1]] = n[1]
    return False





print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))



