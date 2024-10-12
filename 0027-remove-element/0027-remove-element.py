class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for num in nums:
            if(num != val):
                temp.append(num)
        k = len(temp)
        for i in range(0, len(temp)):
            nums[i] = temp[i]
        
        return k