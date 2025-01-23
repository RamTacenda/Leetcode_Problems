class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        row, col = [0]*n, [0]*m
        for i in range(0, n):
            for j in range(0, m):
                if(grid[i][j] == 1):
                    row[i] += 1
                    col[j] += 1

        count = 0
        for i in range(0, n):
            for j in range(0, m):
                if(grid[i][j] == 1):
                    if(row[i] > 1 or col[j] > 1):
                        count += 1

        return count