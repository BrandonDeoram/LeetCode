
hashMap = {}

def twoSum(nums, target):
    for i,n in enumerate (nums):
        diff = target - n
        #9-2 in the hashmap then grab it and return it
        if(diff in hashMap):
            return [hashMap[diff],i]
        hashMap[n] = i
    return 


nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))

# 9-2 = 7     -> 7 in hashmap no -> 2:0

#9-7 = 2 -> is 2 in hashMap yes  