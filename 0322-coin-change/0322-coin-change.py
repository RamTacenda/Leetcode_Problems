class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount == 0):
            return 0

        res = float('inf')    
        check = False    
        def combSum(idx, ds, target):
            nonlocal res
            nonlocal check
            if(idx == len(coins)):
                if(target == 0):
                    check = True
                    res = min(res, len(ds))
                return

            if(coins[idx] <= target):
                ds.append(coins[idx])
                combSum(idx, ds, (target-coins[idx]))
                ds.pop()

            combSum(idx+1, ds, target)

        combSum(0, [], amount)
        if not check:
            return -1
        return res