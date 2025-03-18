class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        path = set()

        def check(i, j, idx):
            if idx == len(word):
                return True
            if(i < 0 or j < 0 or \
            i == n or j == m or\
            word[idx] != board[i][j] or\
            (i, j) in path):
                return False
            
            path.add((i, j))
            res = (check(i+1, j, idx+1) or
                    check(i-1, j, idx+1) or
                    check(i, j+1, idx+1) or 
                    check(i, j-1, idx+1))
            path.remove((i, j))
            return res

        for i in range(0, n):
            for j in range(0, m):
                if check(i, j, 0):
                    return True

        return False