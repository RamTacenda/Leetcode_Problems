class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if(nums[i] != nums[i-1]+1):
                prefixsum = sum(nums[0:i])
                while True:
                    if(prefixsum not in nums):
                        return prefixsum
                    prefixsum += 1
        return sum(nums) if (len(nums) > 1) else sum(nums)+1