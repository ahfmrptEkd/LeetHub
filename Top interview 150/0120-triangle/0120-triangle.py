class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 삼각형의 높이
        n = len(triangle)
        
        # 각 위치까지의 최소 경로 합을 저장할 DP 테이블 초기화
        # dp[i][j]는 위치 (i,j)까지의 최소 경로 합
        dp = [[0] * (i + 1) for i in range(n)]
        
        # 시작점 초기화
        dp[0][0] = triangle[0][0]
        
        # 위에서 아래로 진행
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:  # 각 행의 첫 번째 원소
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:  # 각 행의 마지막 원소
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:  # 그 외 중간 원소
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        # 마지막 행에서 최소값 찾아 반환
        return min(dp[-1])