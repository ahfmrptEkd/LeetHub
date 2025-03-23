class Solution:
    def totalNQueens(self, n: int) -> int:

        def backtrack(queens: set, row: int) -> int:
            if row == n:
                return 1

            total = 0

            for col in range(n):
                if col in queens or (row + col) in right_diagonal or (row - col) in left_diagonal:
                    continue
                
                queens.add(col)
                left_diagonal.add(row - col)
                right_diagonal.add(row + col)

                total += backtrack(queens, row+1)
                
                queens.remove(col)
                left_diagonal.remove(row - col)
                right_diagonal.remove(row + col)

            return total

        queens = set()
        left_diagonal = set()
        right_diagonal = set()
        
        ans = backtrack(queens, 0)

        return ans