class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        memo = {0:0}

        def min_coins(amt):
            if amt in memo:
                return memo[amt]
            
            minn = float('inf')
            for coin in coins:
                diff = amt-coin
                if diff < 0:
                    break
                
                minn = min(minn, 1 + min_coins(diff))
            
            memo[amt] = minn
            return minn
        
        res = min_coins(amount)
        if(res == float('inf')):
            return -1
        return res