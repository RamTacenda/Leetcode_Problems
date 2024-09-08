class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mapp = dict()
        for i in nums:
            if(i not in mapp):
                mapp[i] = 1
            else:
                mapp[i] += 1
        
        res = list(sorted(mapp.items(), key = lambda x: x[1], reverse = True))
        return res[0][0]