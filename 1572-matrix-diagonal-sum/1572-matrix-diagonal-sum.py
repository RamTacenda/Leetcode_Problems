class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if(i==j or (i+j) == len(mat)-1):
                    summ += mat[i][j]

        return summ