class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 기본 조건 검사: 길이가 맞지 않으면 인터리빙이 불가능
        if len(s1) + len(s2) != len(s3):
            return False
        
        # 더 짧은 문자열을 s2로 설정하여 메모리 사용 최소화
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            
        # 1D DP 배열 사용 (공간 복잡도 O(n))
        dp = [False] * (len(s2) + 1)
        
        # 초기화: 빈 문자열끼리는 인터리빙 가능
        dp[0] = True
        
        # s1이 빈 경우 초기화 (s2만으로 s3 형성 가능한지)
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        
        # 동적 계획법으로 모든 경우의 수 계산
        for i in range(1, len(s1) + 1):
            # 첫 번째 열 업데이트 (s1만으로 s3 형성 가능한지)
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            
            # 나머지 열 업데이트
            for j in range(1, len(s2) + 1):
                # 현재 위치(i+j-1)의 s3 문자가 s1 또는 s2의 현재 문자와 일치하는지
                s1_match = dp[j] and s1[i-1] == s3[i+j-1]  # 이전 행의 같은 열
                s2_match = dp[j-1] and s2[j-1] == s3[i+j-1]  # 현재 행의 이전 열
                
                # 두 경우 중 하나라도 성립하면 인터리빙 가능
                dp[j] = s1_match or s2_match
        
        # 최종 결과
        return dp[len(s2)]