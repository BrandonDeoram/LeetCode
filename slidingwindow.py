import math

#Return the largest sum due to window size 
arr =[4,2,1,7,8,1,2,8,1,0]

maxSum = float('-inf')
sum = 0

for x in range(0,len(arr)):
    sum +=arr[x]
    if(x >=2):
        maxSum = max(maxSum,sum)
        sum-= arr[x-2]
print(maxSum)

#Return the smallest window size of target value 
winSize = float('inf')
target = 8
currSum = 0
winStart = 0
arr =[4,2,1,7,8,1,2,8,1,0]

for x in range(len(arr)):
    currSum+=arr[x]
    #Shrinking left side
    while(currSum>=target):
        winSize = min(winSize,x-winStart+1)
        currSum-=arr[winStart]
        winStart+=1
print(winSize)
