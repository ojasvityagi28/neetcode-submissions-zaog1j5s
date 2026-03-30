class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] not in rows[r] and board[r][c] not in columns[c] and board[r][c] not in boxes[(r//3,c//3)]):
                    rows[r].add(board[r][c])
                    columns[c].add(board[r][c])
                    boxes[(r//3,c//3)].add(board[r][c])
                else:
                    return False
        return True


        