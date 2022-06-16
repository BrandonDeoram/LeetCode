from turtle import left


prices = [1,2,4,2,5,7,2,4,9,0,9]

buy = 0
sell = 1
maxProfit = 0
curr = 0
counter=0
while(sell<len(prices)):
    if(prices[buy]<prices[sell]):
        curr = prices[sell]-prices[buy]
        maxProfit = max(maxProfit,curr)
    else:
        buy=sell
    sell+=1
print(maxProfit)