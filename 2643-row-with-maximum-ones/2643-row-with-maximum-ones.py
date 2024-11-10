class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx = 0
        maxx = float('-inf')
        for row in range(0, len(mat)):
            summ = sum(mat[row])
            if(summ > maxx):
                maxx = summ
                idx = row

        return [idx, maxx]
