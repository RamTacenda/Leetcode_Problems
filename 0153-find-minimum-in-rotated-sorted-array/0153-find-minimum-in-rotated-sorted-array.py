class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if(nums[l] <= nums[r]): return nums[l]
        while(l <= r):
            mid = (l+r)//2
            if(nums[mid] > nums[mid+1]):
                return nums[mid+1]
            if(nums[mid-1] > nums[mid]):
                return nums[mid]

            if(nums[mid] > nums[0]):
                l = mid+1
            else:
                r = mid-1

            