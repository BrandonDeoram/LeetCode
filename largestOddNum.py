# First if the whole number itself is odd num

# if it is
# then return string

# else
# run a for loop that does sliding window and see if each substring is an odd number or not

num = "52"


def largestOddNumber(num):
    i = len(num) -1
    while i >= 0 and int(num[i])%2 == 0:
        i-=1
    return num[:i+1]
print(largestOddNumber(num))

#Sliding window
    # curr = ""
    # maxNum = float("-inf")
    # if(int(num) % 2 == 1):
    #     return num
    # else:
    #     for i in range(len(num)):
    #         curr += num[i]
    #         if i+1 < len(num) and int(curr) % 2 == 1:
    #             maxNum = max(int(curr), maxNum)
    # if(str(maxNum) == "-inf"):
    #     return ""
    # return str(maxNum)