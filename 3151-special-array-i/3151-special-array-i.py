class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if(len(nums) == 1): return True
        for i in range(0, len(nums)-1):
            p1, p2 = nums[i], nums[i+1]
            if(p1&1 == p2&1):
                return False
        return True