class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        r = set()
        c = set()

        for row_i, row_v in enumerate(matrix):
            print(row_i, row_v)

            for col_i, col_v in enumerate(row_v):
                print("\n", col_i, col_v)

                if col_v == 0:
                    r.add(row_i)
                    c.add(col_i)
        print(r, c)

        for i in range(n):
            for j in range(m):
                if i in r or j in c:
                    matrix[i][j] = 0