class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if(0 <= nr < N and 0 <= nc < M and \
                     grid[nr][nc] == '1' and (nr,nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        
        N, M = len(grid), len(grid[0])
        visited = set()
        directions = [[-1,0], [1,0], [0, 1], [0, -1]]
        count = 0
        for r in range(0, N):
            for c in range(0, M):
                if(grid[r][c] == '1' and (r, c) not in visited):
                    bfs(r, c)
                    count += 1

        return count