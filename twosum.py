from functools import reduce


def twosum(nums, target):
    prevMap = {}  # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


print(twosum([1, 1, 3, 4, 3, 6], 6))
print(twosum([3, 2, 4], 6))
