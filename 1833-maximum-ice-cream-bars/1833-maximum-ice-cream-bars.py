class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for price in costs:
            if(coins == 0):
                return count
            if(price <= coins):
                count += 1
                coins = coins - price
            
        return count