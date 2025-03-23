class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(start, memo=None):
            if memo is None:
                memo = {}

            # 문자열 끝까지 도착한다면 성공
            if start == len(s):
                return True
            
            # 이미 확인 한 부분은 결과 반환
            if start in memo:
                return memo[start]
            
            for w in wordDict:
                if s[start:].startswith(w):
                    if dp(start + len(w), memo):
                        memo[start] = True
                        return True
            
            memo[start] = False
            return False

        return dp(0)