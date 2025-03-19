class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = list()

        for i in range(0, 9):
            for j in range(0, 9):
                if(board[i][j] != '.'):
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    box_idx = (i//3)*3 + (j//3)
                    boxes[box_idx].add(num)
                else:
                    empty_cells.append((i, j))

        def solve(idx):
            if idx == len(empty_cells):
                return True
            
            i, j = empty_cells[idx]
            box_idx = (i//3)*3 + (j//3)

            for c in "123456789":
                if(c not in rows[i] and
                    c not in cols[j] and 
                    c not in boxes[box_idx]):
                    board[i][j] = c
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[box_idx].add(c)

                    if(solve(idx+1)):
                        return True

                    board[i][j] = '.'
                    rows[i].remove(c)
                    cols[j].remove(c)
                    boxes[box_idx].remove(c)
            
            return False

        solve(0)