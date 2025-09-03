class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        mapp = defaultdict(list)

        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums[i])-1, -1, -1):
                mapp[i+j].append(nums[i][j])
        
        for i in range(0, len(mapp)):
            ans.extend(mapp[i])
        
        return ans