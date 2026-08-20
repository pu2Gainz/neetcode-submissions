class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        boarder = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]    

        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS and (r, c) not in boarder and board[r][c] == "O"):
                return
            boarder.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

         # Top and bottom rows
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        # Left and right columns
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for r in range(ROWS): 
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in boarder:
                    board[r][c] = "X"

        


        

