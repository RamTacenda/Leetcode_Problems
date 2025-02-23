class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = dict()
        for i in nums:
            mapp[i] = mapp.get(i, 0) + 1
        sorted_ls, ans = sorted(mapp.items(), key = lambda x: x[1]), list()
        print(sorted_ls)
        for i in range(1, k+1):
            ans.append(sorted_ls[-i][0])
        return ans
