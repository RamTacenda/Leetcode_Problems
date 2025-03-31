class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pairs = len(nums) // 2
        mapp = dict()
        for n in nums:
            mapp[n] = mapp.get(n, 0) + 1
        
        for vals in mapp.values():
            if vals & 1 == 1:
                return False
        return True