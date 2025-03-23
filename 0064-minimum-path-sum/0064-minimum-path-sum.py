class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 그리드의 크기를 가져옴
        m, n = len(grid), len(grid[0])      
        # dp 배열 초기화: 모든 원소를 무한대로 설정 (각 위치에서 '위에서 오는 경로'가 없는 것으로 초기화)
        dp = [float('inf')] * n
        
        # 시작점의 이전 상태를 0으로 설정 (첫 번째 칸의 값만 추가될 수 있도록)
        dp[0] = 0

        # 그리드의 모든 위치를 순회
        for i in range(m):
            for j in range(n):
                if j > 0:
                    # 현재 위치(i,j)까지의 최소 경로 합을 계산
                    # min(dp[j], dp[j-1])은 "위에서 오는 경로"와 "왼쪽에서 오는 경로" 중 최소값
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
                else:
                    # 첫 번째 열의 경우, 위에서만 올 수 있음
                    dp[j] = dp[j] + grid[i][j]

        # 오른쪽 하단까지의 최소 경로 합 반환
        return dp[-1]