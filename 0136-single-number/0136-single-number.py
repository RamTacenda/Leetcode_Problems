class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapp = dict()
        for num in nums:
            if num in mapp:
                mapp[num] += 1
            else:
                mapp[num] = 1
        
        for num, freq in mapp.items():
            if(freq == 1):
                return num