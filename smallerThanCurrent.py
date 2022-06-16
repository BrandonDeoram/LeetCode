from multiprocessing.sharedctypes import Value


nums = [8,1,2,2,3]
# temp = og.copy()
# indexList = []
# for i in og:
#     newList = list(filter(lambda x: x < i,temp))
#     indexList.append(len(newList))
# newList = []

# counter = 0
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if(nums[j]<nums[i] and j!=i):
#             counter+=1
    
#     newList.append(counter)
#     counter=0

#Sort the list 

#[1,2,2,3,8]

#dictvalue = [0,1,3,4]
dict = {}
ans = []
for index,value in enumerate(sorted(nums)):
    if(value not in dict):
        dict[value] = index
ans = []
#gets corresponding value 
for value in nums:
    ans.append(dict[value])

print(ans)

    
