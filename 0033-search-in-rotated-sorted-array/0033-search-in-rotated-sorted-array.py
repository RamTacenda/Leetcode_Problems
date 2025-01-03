class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        l, r = 0, len(nums)-1
        while(l <= r):
            mid = (l+r)//2
            if(target == nums[mid]):
                return mid

            # Left sorted portion of the array [4,5,6,7]
            if(nums[l] <= nums[mid]):
                if(target > nums[mid] or target < nums[l]):
                    l = mid + 1
                else:
                    r = mid - 1
            
            # Right sorted portion of the array [0,1,2,3]
            else:
                if(target < nums[mid] or target > nums[r]):
                    r = mid - 1
                else:
                    l = mid + 1