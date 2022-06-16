
# def maxProfit(prices):
#     maxNum = 0
#     min = 1000000000
#     for x in prices:
#         if (x < min):
#             #seen a value smaller
#             min = x
#         else:
#             #calc value if were gonn make more money or not
#             maxNum = max(maxNum,x-min)
#     return maxNum

def maxProfit(prices):
    maxVal = 0
    min =100000
    for i in range(len(prices)):
        5 < 1
        if(prices[i] < min):
            
            min = prices[i]
        else:
            maxVal = max(maxVal,prices[i]-min)
    return maxVal
print(maxProfit([7, 1, 5, 3, 6, 4]))

