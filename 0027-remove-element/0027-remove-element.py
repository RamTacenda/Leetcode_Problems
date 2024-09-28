class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        num = 0
        while(num < count):
            nums.remove(val)
            num += 1
        
        return len(nums)