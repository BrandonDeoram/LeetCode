from collections import Counter
def longestConsecutive(nums):
    hashMap = Counter(nums)
    return hashMap

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
