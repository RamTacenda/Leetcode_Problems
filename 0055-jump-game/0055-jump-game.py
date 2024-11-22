class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxind = 0

        for i in range(0, len(nums)):
            if(i > maxind):
                return False
            maxind = max(maxind, i+nums[i])

        return True