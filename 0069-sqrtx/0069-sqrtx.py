class Solution:
    def mySqrt(self, x: int) -> int:
        if(x == 1): return 1

        low = 1
        high = x//2
        ans = 0

        while(low <= high):
            mid = (low + high)//2
            if(mid*mid > x):
                high = mid -1
            elif(mid*mid <= x):
                ans = mid
                low =  mid + 1

        return ans