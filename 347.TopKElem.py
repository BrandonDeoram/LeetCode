from collections import Counter


def topKFrequent(nums, k):
    freqList = []
    freq = Counter(nums)
    temp = k
    for key, value in sorted(freq.items(), key=lambda item: item[1],reverse=True):
        if(temp>0):
            freqList.append(key)
            temp-=1
    return freqList


# print(topKFrequent([1,1,1,2,2,3],2))
# print(topKFrequent([1,2],2))
# print(topKFrequent([3,0,1,0]
# ,1))

print(topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10))
