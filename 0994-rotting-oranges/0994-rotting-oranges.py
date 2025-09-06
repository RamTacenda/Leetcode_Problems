class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        N, M = len(grid), len(grid[0])
        num_fresh = 0
        minutes = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]==1:
                    num_fresh += 1
                elif grid[i][j]==2:
                    q.append((i,j))
        
        if num_fresh==0:
            return 0

        while q:
            for _ in range(0, len(q)):
                r, c = q.pop()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if(0<=nr<N and 0<=nc<M and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        num_fresh -= 1
                        q.append((nr, nc))
            
            minutes += 1

        if num_fresh!=0:
            return -1
        return minutes