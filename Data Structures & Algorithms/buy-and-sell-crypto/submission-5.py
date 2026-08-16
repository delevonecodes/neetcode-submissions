class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            current_profit = prices[r] - prices[l]
            max_profit = max(max_profit, current_profit)
            if prices[r] < prices[l]:
                l = r
            r+= 1
            
        return max_profit
            

