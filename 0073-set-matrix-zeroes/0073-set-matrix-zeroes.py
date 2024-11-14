class Solution:
    def row(self, mat, i, j):
        for j in range(0, len(mat[0])):
            if(mat[i][j] != 0):
                mat[i][j] = "signal"

    def col(self, mat, i, j):
        for i in range(0, len(mat)):
            if(mat[i][j] != 0):
                mat[i][j] = "signal"

    def setZeroes(self, mat: List[List[int]]) -> None:
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if(mat[i][j] == 0):
                    self.row(mat, i, j)
                    self.col(mat, i, j)

        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if(mat[i][j] == "signal"):
                    mat[i][j] = 0