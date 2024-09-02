class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currsum = 0
        ans = len(nums)
        l = 0
        f = False

        for r in range(0, len(nums)):
            currsum += nums[r]
            if(currsum >= target):
                f = True
                while(currsum - nums[l] >= target):
                    currsum -= nums[l]
                    l += 1
                ans = min(ans, r-l+1)

        return ans if f else 0