class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search
        left, right = 0, len(nums)-1
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if(nums[mid] <= target):
                ans = mid
                left = mid + 1
            elif(nums[mid] > target):
                right = mid - 1
        return ans if(nums[ans] == target) else -1