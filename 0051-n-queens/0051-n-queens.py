class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                res.append(["".join(item) for item in board])
            
            for col in range(n):
                if col in queens or (row-col) in left_diagonal or (row+col) in right_diagonal:
                    continue
                
                queens.add(col)
                left_diagonal.add(row-col)
                right_diagonal.add(row+col)
                board[row][col] = "Q"

                backtrack(row + 1)

                queens.remove(col)
                left_diagonal.remove(row-col)
                right_diagonal.remove(row+col)
                board[row][col] = "."

        queens = set()
        left_diagonal = set()
        right_diagonal = set()
        board = [["." for _ in range(n)] for _ in range(n)]
        res =  []
        backtrack(0)

        return res