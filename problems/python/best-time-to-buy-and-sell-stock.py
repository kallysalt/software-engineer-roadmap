# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        
       # solution 1: brute force - calculate the return for every posible senerio
       # 7-1,7-5, ..., 7-4, 1-5, 1-3, ..., 1-4, .. 6-4
       # time complexity: (n-1)+(n-2)+...+1 ~ n^2

        # res = 0
        # n = len(prices)

        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         buy = prices[i]
        #         sell = prices[j]
        #         profit = sell - buy
        #         res = max(res, profit)
        
        # return res

        # solution 2: optimize performamce by minimizing redundant computations
        # for a given sell price, only calculate the profit if we iterate to a 
        # lower buy price
        # time complexity: n^2
        
        # res = 0
        # n = len(prices)

        # for r in range(n - 1, 0, -1):
        #     sellPrice = prices[r]
        #     # calculate profit if : buyPrice < sellPrice, buyPirce < previous buyPirce
        #     prevBuyPrice = sellPrice
        #     for l in range(r):
        #         buyPrice = prices[l]
        #         if buyPrice < sellPrice and buyPrice < prevBuyPrice:
        #             profit = sellPrice - buyPrice
        #             res = max(res, profit)
        
        # return res if res > 0 else 0

        # solution 3: can we identify max profit in one pass?
        # for each price, record the lowest price before it

        # we can maintain an arr that stores the lowest price we've seen so far
        # [7,1,5,3,6,4]
        #  7 7 1 1 1 1

        # n = len(prices)
        # arr = [prices[0]]
        # lowest = prices[0]
        # for i in range(1, n):
        #     arr.append(lowest)
        #     lowest = min(lowest, prices[i])
        #     profit = prices[i] - lowest
        
        # # at every price point, profit = price - lowest price we've seen so far
        # res = 0
        # for i in range(n):
        #     profit = prices[i] - arr[i]
        #     res = max(res, profit)
        # return res

        # solution 4: optimize space complexity for 3
        
        lowest = prices[0]
        res = 0

        for price in prices[1:]:
            # calculate profit
            profit = price - lowest
            res = max(res, profit)
            # update lowest
            lowest = min(lowest, price)
        
        return res

        