class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 0:
            return 0
        
        buy = prices[0]
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            profit = max(profit, prices[i] - buy)
        
        return profit