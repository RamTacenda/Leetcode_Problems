class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        dist = [[0 for _ in range(0, m)] for _ in range(0, n)]
        vist = [[0 for _ in range(0, m)] for _ in range(0, n)]
        queue = list()

        for i in range(0, n):
            for j in range(0, m):
                if(isWater[i][j] == 1):
                    queue.append([(i,j), 0])
                    vist[i][j] = 1

        rowmove = [-1, 0, 1, 0]
        colmove = [0, 1, 0, -1]

        while queue:
            row = queue[0][0][0]
            col = queue[0][0][1]
            steps = queue[0][1]
            queue.pop(0)

            dist[row][col] = steps

            for i in range(0, 4):
                nrow = row + rowmove[i]
                ncol = col + colmove[i]
                if(nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and vist[nrow][ncol] == 0):
                    vist[nrow][ncol] = 1
                    queue.append([(nrow, ncol), steps+1])

        return dist