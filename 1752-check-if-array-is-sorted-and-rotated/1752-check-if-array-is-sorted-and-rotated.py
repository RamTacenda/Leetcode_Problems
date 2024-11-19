class Solution:
    def check(self, nums: List[int]) -> bool:

        for i in range(0, len(nums)):
            temp = nums[0]
            for j in range(1, len(nums)):
                nums[j-1] = nums[j]
            nums[-1] = temp

            if(sorted(nums) == nums):
                return True
        
        return False