def maxProfit(prices):
    lowest = prices[0]
    # [7,1,5,3]

    for price in prices:
        if(price < lowest):
            lowest = price
        res = max(res, price - lowest)
    print(res)


prices = [7, 1, 5, 3, 6, 4]
maxProfit(prices)
