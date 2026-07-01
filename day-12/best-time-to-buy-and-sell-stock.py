def maxProfit(self, prices):
    l, r = 0, 1
    maxProfit = 0

    
    while r < len(prices):
        profit = prices[r] - prices[l]
        if profit < 0:
            l = r 
            r += 1
        else:
            maxProfit = max(profit, maxProfit)
            r += 1 
    return maxProfit


# OR


# class Solution(object):
#     def maxProfit(self, prices):
#         min_price = prices[0]
#         max_profit = 0

#         for price in prices:
#             if price < min_price:
#                 min_price = price

#             profit = price - min_price

#             if profit > max_profit:
#                 max_profit = profit

#         return max_profit