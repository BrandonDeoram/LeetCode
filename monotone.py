
def isMonotonic(nums):
    
    check = []
    for i in range(len(nums)):
        nums[i] =check[i]

    check.sort()
    if(check == nums):
        return True
    check.reverse()
    if(check == nums):
        return True


print(isMonotonic([1,3,2]))




#Remove dup
#sort max = [9,8,7,5,4,2]
#sort low = [2,4,6,7,8,9]

#(9*8)-(2*4)