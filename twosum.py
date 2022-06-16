from functools import reduce



# def twosum(nums, target):
#     for x in range(len(nums)):
#         for y in range(len(nums)):
#             if(x == y):
#                 continue
#             if(nums[x] + nums[y] == target):

#                 first = list(nums).index(nums[x])
#                 second = list(nums).index(nums[y])

#                 return first, second
#             else:
#                 continue


# print(twosum([2,7,60,23], 9))


# another solution using target value

# def twosum(nums, target):

#  for i in range(len(nums)):
#     if (target - nums[i]) in nums:
#         if nums.index(target - nums[i]) != i:
#             return nums.index(target - nums[i]),i


# print(twosum([3,3],6))
# print(twosum([3,2,4],6))
