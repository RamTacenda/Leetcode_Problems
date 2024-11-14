class Solution:

    def merge(self, low, mid, high, nums):
        temp = []
        left, right = low, mid+1

        while(left <= mid and right <= high):
            if(nums[left] < nums[right]):
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        
        while(left <= mid):
            temp.append(nums[left])
            left += 1

        while(right <= high):
            temp.append(nums[right])
            right += 1

        for i in range(0, len(temp)):
            nums[low + i] = temp[i]
    
    def mergesort(self, low, high, nums):
        if(low >= high):
            return
        mid = (low + high)//2
        self.mergesort(low, mid, nums)
        self.mergesort(mid+1, high, nums)
        self.merge(low, mid, high, nums)

    def sortColors(self, nums: List[int]) -> None:
        low, high = 0, len(nums)-1
        self.mergesort(low, high, nums)
        