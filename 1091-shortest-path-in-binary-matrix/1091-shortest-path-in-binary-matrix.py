class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0, 0, 1)]) # r, c, length
        path = set((0,0))
        directions = [[0,1], [0,-1], [-1,0], [1,0], [1,1],
                        [-1,-1], [-1,1], [1,-1]] # 8 directions

        while q:
            r, c, length = q.popleft()
            if(min(r,c) < 0 or max(r,c) == N or grid[r][c]):
                continue
            if((r,c) == (N-1, N-1)):
                return length
            
            # Traversing every directions
            for dr, dc in directions:
                if((r+dr, c+dc) not in path):
                    path.add((r+dr, c+dc))
                    q.append((r+dr, c+dc, length+1))

        return -1