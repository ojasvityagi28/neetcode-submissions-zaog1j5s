class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows , cols = len(board) ,len(board[0])
        q = []
        directions = [(1, 0) , (-1 , 0) , (0 , 1) , (0 , -1)]
        for r in range(rows):
            if board[r][0] == "O":
                q.append((r , 0))
                board[r][0] = "S"
            if board[r][cols - 1] == "O":
                q.append((r , cols - 1))
                board[r][cols - 1] = "S"
        for c in range(cols):
            if board[0][c] == "O":
                q.append((0, c))
                board[0][c] = "S"
            if board[rows - 1][c] == "O":
                q.append((rows - 1, c))
                board[rows - 1][c] = "S"
        q = deque(q)
        while q:
            r , c = q.popleft()
            for dr, dc  in directions:
                nr , nc = r + dr , c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    q.append((nr , nc))
                    board[nr][nc] = "S"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
    
                



        