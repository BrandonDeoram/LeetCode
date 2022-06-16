nums = [0, 1, 2, 5, 8, 10]

# Iterate over nums
# Check to see if the first number is +1 over i+1 if it is add that number to as a string and append to list
# if its not just add number to list
start = nums[0]
end = 0
newList = []
holder = ""
counter = 1
add = True
number = 0
for x in range(len(nums)-1):
    number = nums[x+1]

    if(nums[x] + counter == nums[x+1]):
        print("hello")

    else:
        print(nums[x])
        if(start == nums[x]):
            newList.append(start)

        else:
            holder = str(start)+"->"+str(nums[x])
            newList.append(holder)
        start = nums[x+1]
        # track ok it end [0,2]
        # set the new end value to or rather nums[x-1]
        # append recent numbers to list
print(newList)
