class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        한번의 이어진 모든 땅을 방문해서 물로 처리
        새로운 이어지지 않은 땅을 만나면 하기.
        """
        def is_valid(y, x, n, m):
            """
            주어진 좌표가 grid 범위 내에 있는지 확인하는 헬퍼 함수
            """
            return 0 <= x < n and 0 <= y < m

        def dfs(y, x):
            """
            DFS로 현재 위치에서 연결된 모든 땅을 탐색하는 함수
            방문한 땅은 물('0')로 변경
            """
            # 베이스 케이스: 범위를 벗어나거나 이미 방문했거나 물인 경우
            if not is_valid(y, x, n, m) or grid[y][x] != "1":
                return

            # 현재 위치 방문 처리
            grid[y][x] = "0"

            # 상하좌우 인접한 땅 탐색
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                dfs(ny, nx)

        # grid의 크기 정의
        m, n = len(grid), len(grid[0])
        
        # 상하좌우 이동 방향 벡터
        dx = [-1, 1, 0, 0]  # x축 이동 (좌우)
        dy = [0, 0, -1, 1]  # y축 이동 (상하)
        
        islands = 0  # 섬 카운터

        # 전체 grid를 순회하며 새로운 섬 탐색
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":  # 새로운 섬 발견
                    islands += 1
                    dfs(i, j)  # 현재 섬과 연결된 모든 땅 탐색
        return islands