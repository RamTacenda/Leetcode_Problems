class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float('inf')
        profit = 0

        for price in prices:
            if(price < minn):
                minn = price
            elif((price-minn) > profit):
                profit = price-minn
        
        return profit