class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float('inf')
        profit = 0

        for i in range(0, len(prices)):
            if(prices[i] < minn):
                minn = prices[i]
            elif(prices[i] - minn > profit):
                profit = prices[i] - minn
        
        return profit