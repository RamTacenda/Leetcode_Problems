class Solution(object):
    def twoSum(self, nums, target):
        mapp = dict()
        for i in range(0, len(nums)):
            req = target - nums[i]
            if(req in mapp):
                return [mapp[req], i]
            mapp[nums[i]] = i