class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        for i in range(0, len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            mapp = set()
            for j in range(i+1, len(nums)):
                rem = -(nums[i] + nums[j])
                if(rem in mapp):
                    ls = [nums[i], nums[j], rem]
                    ls.sort()
                    if(ls not in ans):
                        ans.append(ls)
                else:
                    mapp.add(nums[j])

        return ans
