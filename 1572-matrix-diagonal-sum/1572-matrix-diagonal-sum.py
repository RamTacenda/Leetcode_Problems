class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ, n = 0, len(mat)
        for i in range(0, len(mat)):
            summ += mat[i][i]
            if(i != n-1-i):
                summ += mat[i][(n-1)-i]

        return summ