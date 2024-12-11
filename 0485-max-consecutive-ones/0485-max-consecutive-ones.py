class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mapp = set()
        temp = 0
        for num in nums:
            if(num == 1):
                temp += 1
            else:
                mapp.add(temp)
                temp = 0
        
        if(temp):
            mapp.add(temp)
            temp = 0

        return max(list(mapp))