class Solution:
    def numTilings(self, n: int) -> int:
        def dp(num, memo={}):           
            if num <= 1:
                return 1
            
            elif num == 2:
                return 2
            
            elif num == 3:
                return 5

            elif num in memo:
                return memo[num]
            
            memo[num] = (2 * dp(num-1) + dp(num-3)) % MOD
            return memo[num]
        
        MOD = 1000000007

        return dp(n)
