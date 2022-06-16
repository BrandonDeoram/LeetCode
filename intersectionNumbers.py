nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

result = []

for x in nums1:
    if(nums2.__contains__(x)):
        result.append(x)
        nums2.remove(x)
print(result)
