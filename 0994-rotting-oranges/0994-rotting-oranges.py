from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # 썩은 오렌지의 위치를 찾아 큐에 추가하고, 신선한 오렌지 개수 세기
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) # row, col, minutes
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_time = 0

        while queue:
            row, col, time = queue.popleft()
            max_time = time

            for dr, dc in directions:
                nx, ny = row + dr, col + dc

                if (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1):
                    # 오렌지를 상하게 변경
                    grid[nx][ny] = 2
                    fresh_count -= 1

                    queue.append((nx, ny, time + 1))
        
        return max_time if fresh_count == 0 else -1
