class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = dict()
        for i in range(0, len(nums)):
            if(nums[i] in mapp):
                if(abs(i-mapp[nums[i]]) <= k):
                    return True
            mapp[nums[i]] = i

        return False