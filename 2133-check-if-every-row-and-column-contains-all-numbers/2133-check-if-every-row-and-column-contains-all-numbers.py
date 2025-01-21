class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(0, n):
            mapp1 = [0] * n
            mapp2 = [0] * n
            for j in range(0, n):
                mapp1[matrix[i][j]-1] = 1
                mapp2[matrix[j][i]-1] = 1
            if(0 in mapp1 or 0 in mapp2):
                return False
        
        return True