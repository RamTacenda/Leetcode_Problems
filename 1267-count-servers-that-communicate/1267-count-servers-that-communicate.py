class Solution:
    def check(self, grid, row, col):
        n, m = len(grid), len(grid[0])
        # row check
        for c in range(0, m):
            if(grid[row][c] == 1 and col != c):
                return True

        # col check
        for r in range(0, n):
            if(grid[r][col] == 1 and row != r):
                return True

        return False

    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(0, n):
            for j in range(0, m):
                if(grid[i][j] == 1):
                    if self.check(grid, i, j):
                        count += 1

        return count

        