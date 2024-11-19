class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        cur_sum, ans = 0, 0
        l = 0

        for r in range(0, len(nums)):
            count[nums[r]] += 1
            cur_sum += nums[r]

            if(r-l+1 > k):
                count[nums[l]] -= 1
                if(count[nums[l]] == 0):
                    count.pop(nums[l])
                cur_sum -= nums[l]
                l += 1
            
            if(r-l+1 == len(count) == k):
                ans = max(ans, cur_sum)

        return ans
