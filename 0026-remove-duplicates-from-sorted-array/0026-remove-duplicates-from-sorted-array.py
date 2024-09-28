class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        for i in nums:
            if(i not in unique):
                unique.append(i)
        
        for j in range(0, len(unique)):
            nums[j] = unique[j]
        
        return len(unique)