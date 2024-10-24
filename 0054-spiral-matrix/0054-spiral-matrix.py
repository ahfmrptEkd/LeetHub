class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = set()
        result = []
        row = col = 0

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        dir = 0

        def valid_pos(row, col):
            return (0 <= row < m and 0 <= col < n and (row, col) not in visited)
        
        while len(visited) < m * n:
            if valid_pos(row, col):
                visited.add((row,col))
                result.append(matrix[row][col])

                # 현재 방향으로 더 해줌.
                next_row = row + directions[dir][0]
                next_col = col + directions[dir][1]
                
                # 다음 스텝 미래를 장막을 들추고 본다.
                if valid_pos(next_row, next_col):
                    row = next_row
                    col = next_col
                else:
                    dir = (dir+1) % 4
                    row += directions[dir][0]
                    col += directions[dir][1]

        return result