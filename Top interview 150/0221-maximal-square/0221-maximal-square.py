class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # 이전 행의 값들
        prev = [0] * n
        max_side = 0
        
        # 첫 행 초기화
        for j in range(n):
            prev[j] = int(matrix[0][j])
            max_side = max(max_side, prev[j])
        
        for i in range(1, m):
            # 현재 행의 값들
            curr = [0] * n
            # 첫 열 초기화
            curr[0] = int(matrix[i][0])
            max_side = max(max_side, curr[0])
            
            for j in range(1, n):
                if matrix[i][j] == "1":
                    # prev[j]는 위쪽 값, curr[j-1]은 왼쪽 값, prev[j-1]은 대각선 위 값
                    curr[j] = min(prev[j], curr[j-1], prev[j-1]) + 1
                    max_side = max(max_side, curr[j])
            
            # 다음 행을 위해 현재 행을 이전 행으로 설정
            prev = curr
        
        return max_side ** 2