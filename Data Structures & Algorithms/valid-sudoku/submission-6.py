class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        row_map = {}
        col_map = {}
        box_map = {}

        for r in range(rows):
            for c in range(cols):
                if r not in row_map:
                    row_map[r] = set()
                if c not in col_map:
                    col_map[c] = set()
                if (r//3,c//3) not in box_map:
                    box_map[(r//3,c//3)] = set()
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in row_map[r]:
                    return False
                else:
                    row_map[r].add(cell)
                if cell in col_map[c]:
                    return False
                else:
                    col_map[c].add(cell)
                if cell in box_map[(r//3,c//3)]:
                    return False
                else:
                    box_map[(r//3,c//3)].add(cell)
        return True
                
                


        