class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ, n = 0, len(mat[0])
        for i in range(0, n):
            summ += mat[i][i]
            if(i == (n-i-1)):
                continue
            summ += mat[i][n-i-1]
        
        return summ