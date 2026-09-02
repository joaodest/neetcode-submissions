class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 999
        profit = 0
        for sell in prices:
            profit = max(sell - buy, profit)
            buy = min(buy, sell)
                
        return profit