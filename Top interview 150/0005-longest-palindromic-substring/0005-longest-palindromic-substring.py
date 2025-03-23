class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
            
        # dp[i][j] = s[i...j]가 팰린드롬인지 여부
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        max_length = 1
        start = 0
        
        # 모든 한 글자는 팰린드롬
        for i in range(n):
            dp[i][i] = True
        
        # 두 글자 팰린드롬 확인
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2
        
        # 세 글자 이상의 팰린드롬 확인
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1  # 끝 인덱스
                
                # s[i+1...j-1]이 팰린드롬이고 s[i]와 s[j]가 같으면 s[i...j]도 팰린드롬
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length
        
        return s[start:start + max_length]