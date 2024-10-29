class Solution:
    def recurPermute(self, nums, idx, ans):
        if(idx == len(nums)):
            ans.append(nums.copy())
            return

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.recurPermute(nums, idx+1, ans)
            nums[i], nums[idx] = nums[idx], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        idx, ans = 0, list()
        self.recurPermute(nums, idx, ans)
        return ans
