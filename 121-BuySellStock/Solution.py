class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = 0
        sellDay = 1
        maxProfit = 0

        while(sellDay < len(prices)):

            if(prices[sellDay]-prices[buyDay] > maxProfit):
                    maxProfit = prices[sellDay]-prices[buyDay]

            if(prices[sellDay]-prices[buyDay] <= 0):
                buyDay = sellDay
                sellDay = buyDay+1

            else:
                sellDay = sellDay + 1

        return maxProfit
