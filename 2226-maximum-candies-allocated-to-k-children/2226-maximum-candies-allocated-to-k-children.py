class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        c = sum(candies) // k
        l, r = 1, c
        while(l <= r):
            mid = (l+r)//2
            summ = 0
            for n in candies:
                summ += (n//mid)
            if summ >= k:
                ans = mid
                l = mid+1
            else:
                r = mid-1
        
        return ans