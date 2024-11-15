class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ, n = 0, len(mat)
        for i in range(0, n):
            summ += mat[i][i]
            if((i,i) != (i,n-1-i)):
                summ += mat[i][n-1-i]
        
        return summ