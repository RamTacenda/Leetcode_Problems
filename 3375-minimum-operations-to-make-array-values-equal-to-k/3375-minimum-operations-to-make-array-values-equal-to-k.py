class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # It will be invalid only when the nums contains a value that is lesser than k
        for num in nums:
            if(num < k):
                return -1

        count = 0
        hashset = set()
        for i in range(0, len(nums)):
            hashset.add(nums[i])

        if k in hashset:
            return len(hashset)-1
        
        else:
            return len(hashset)