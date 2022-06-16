nums = [1, 2, 3, 1]

hashMap = {}
if(len(nums)==1):
    print('false')
for x in nums:
    if(x in hashMap):
        print('true')
    else:
        hashMap[x] = 1

