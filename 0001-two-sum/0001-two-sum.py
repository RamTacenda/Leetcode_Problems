class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapp = dict()
        for i in range(0, len(nums)):
            req = target - nums[i]
            if(req in mapp):
                return [mapp[req], i]
            mapp[nums[i]] = i
