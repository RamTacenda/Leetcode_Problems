class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        dist, vist = [[0 for _ in range(0, m)] for _ in range(0, n)], [[0 for _ in range(0, m)] for _ in range(0, n)]
        queue = deque()
        for i in range(0, n):
            for j in range(0, m):
                if(mat[i][j] == 0):
                    queue.append([(i, j), 0])
                    vist[i][j] = 1
                else:
                    vist[i][j] = 0

        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        while queue:
            row = queue[0][0][0]
            col = queue[0][0][1]
            steps = queue[0][1]
            queue.popleft()

            dist[row][col] = steps
            
            for i in range(0, 4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                if(nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and vist[nrow][ncol] == 0):
                    vist[nrow][ncol] = 1
                    queue.append([(nrow, ncol), steps+1])

        return dist