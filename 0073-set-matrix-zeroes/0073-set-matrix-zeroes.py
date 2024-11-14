class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        row = [False]*(len(mat))
        col = [False]*(len(mat[0]))

        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if(mat[i][j] == 0):
                    row[i] = True
                    col[j] = True

        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if(row[i] == True or col[j] == True):
                    mat[i][j] = 0