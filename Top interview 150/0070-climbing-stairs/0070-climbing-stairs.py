class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climb(n, memo={}):
            # 이미 계산 된 값이 있으면 반환
            if n in memo:
                return memo[n]
            
            # 기본 케이스
            if n == 1:
                return 1
            elif n == 2:
                return 2
            
            # 새로운 값 계산하고 메모에 저장
            memo[n] = climb(n-2, memo) + climb(n-1, memo)

            return memo[n]
        
        return climb(n)