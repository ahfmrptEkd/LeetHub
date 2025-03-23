class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid) # n x n grid
        c = [[0] * n for _ in range(n)]
        freq = dict()
        res = 0

        for i in range(n): # 0
            for j in range(n): # 0,1,2,
                c[i][j] = grid[j][i]
        
        for i in c:
            freq[tuple(i)] = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i] == c[j]:
                    key = tuple(grid[i])
                    freq[key] += 1
                    
        res = sum(freq.values())
        return res