class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            p = prices[i] - minn
            profit = max(profit, p)
            minn = min(minn, prices[i])

        return profit
            
