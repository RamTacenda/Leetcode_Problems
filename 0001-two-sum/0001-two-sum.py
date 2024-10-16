class Solution(object):
    def twoSum(self, nums, target):
        mapp = dict()
        for i in range(0, len(nums)):
            rem = target - nums[i]
            if(rem in mapp):
                return [mapp[rem], i]
            mapp[nums[i]] = i