class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result
        
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        dir = 0  # 0: right, 1: down, 2: left, 3: up
        
        while top <= bottom and left <= right:
            if dir == 0:  # Going right
                for j in range(left, right + 1):
                    result.append(matrix[top][j])
                top += 1
            elif dir == 1:  # Going down
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1
            elif dir == 2:  # Going left
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            else:  # Going up
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
            
            dir = (dir + 1) % 4
        
        return result