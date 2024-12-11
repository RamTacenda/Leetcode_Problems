class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(not nums): return 0
        nums = sorted(list(set(nums)))
        mapp = set()
        temp, check = 1, nums[0]
        for num in nums[1:]:
            if(check+1 == num):
                temp += 1
                check = num
            else:
                mapp.add(temp)
                check = num
                temp = 1
        mapp.add(temp)

        print(nums, mapp)
        return max(list(mapp))