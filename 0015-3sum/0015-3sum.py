class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)):
            if(i != 0 and nums[i] == nums[i-1]):
                continue
            mapp = set()
            for j in range(i+1, len(nums)):
                req = -(nums[i] + nums[j])
                temp = [nums[i], req, nums[j]]
                if(req in mapp and temp not in res):
                    res.append(temp)
                else:
                    mapp.add(nums[j])

        return res