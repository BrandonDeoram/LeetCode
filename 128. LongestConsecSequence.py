def longestConsecutive(nums):
    maxLength=0
    length=0
    hashSet=set(nums)
    for num in hashSet:
        # Starting of a Sequence
        if((num-1) not in hashSet):
            while((num)+length in hashSet):
                print('in')
                length+=1
                maxLength = max(length,maxLength)
            length=0
    return maxLength

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
