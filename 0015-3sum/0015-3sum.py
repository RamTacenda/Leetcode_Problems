class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(0, len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            mapp = set()
            for j in range(i+1, len(nums)):
                req = 0 - (nums[i]+nums[j])
                if(req in mapp):
                    triplet = [nums[i], req, nums[j]]
                    triplet.sort()
                    if(triplet not in res):
                        res.append(triplet)
                else:
                    mapp.add(nums[j])

        return res