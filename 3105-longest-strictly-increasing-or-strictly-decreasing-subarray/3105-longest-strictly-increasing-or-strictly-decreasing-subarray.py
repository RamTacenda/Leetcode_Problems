class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
            n = len(nums)

            if(n == 1): return 1
            inc = float('-inf')
            for i in range(0, n-1):
                j, count1 = i, 1
                while j < n-1 and nums[j] < nums[j+1]:
                    count1 += 1
                    j += 1
                inc = max(inc, count1)

            dec = float('-inf')
            for i in range(0, n-1):
                j, count2 = i, 1
                while j < n-1 and nums[j] > nums[j+1]:
                    count2 += 1
                    j += 1
                dec = max(dec, count2)

            return max(dec, inc)