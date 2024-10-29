class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        # Finding the break point
        idx = -1
        for i in range(len(nums)-2, -1, -1):
            if(nums[i] < nums[i+1]):
                idx = i
                break

        if(idx == -1):
            nums[::] = nums[::-1]
            return

        # Swapping the smaller number and idx
        for i in range(len(nums)-1, idx, -1):
            if(nums[i] > nums[idx]):
                nums[idx], nums[i] = nums[i], nums[idx]
                break

        # nums[idx+1: ] = nums[idx+1: ][::-1]
        rev = nums[idx+1:][::-1]
        for i in range(0, len(rev)):
            nums[i+idx+1] = rev[i]