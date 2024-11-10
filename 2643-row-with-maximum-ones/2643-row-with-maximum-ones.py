class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = list()
        maxx = float('-inf')
        for row in range(0, len(mat)):
            c = mat[row].count(1)
            if(c > maxx):
                maxx = c
                ans.append([row, c])

        return ans[-1]
