# def maxProduct(numbers):
#     #sort the array
#     numbers.sort(reverse=True)
#     #loop through i and pick i and i+1 do operations
#     return (numbers[0]-1) *(numbers[1]-1) 
#Runtime 70ms

def maxProduct(nums):
    maxProd = 0
    for i in range(0,len(nums)):
        for j in range(0,len(nums)-1):
            if(i!=j):
                num = (nums[i]-1)*(nums[j]-1)
                maxProd = max(num,maxProd)    
    return maxProd


numbers = [3,4,5,2]
print(maxProduct(numbers))

#(3-1)*(4-1)