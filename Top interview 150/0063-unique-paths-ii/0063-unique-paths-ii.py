class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        # 시작점이 장애물이면 바로 0 반환
        if obstacleGrid[0][0] == 1:
            return 0
            
        dp[0][0] = 1
        
        # 첫 번째 행 초기화
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
            
        # 첫 번째 열 초기화
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
            
        # 나머지 격자 채우기
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) if obstacleGrid[i][j] == 0 else 0
                
        return dp[m-1][n-1]