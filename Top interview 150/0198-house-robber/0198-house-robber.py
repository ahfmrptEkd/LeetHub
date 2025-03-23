class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(n, memo={}):

            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            
            # i번째 집을 털 경우: i번째 집의 돈 + i-2까지의 최대값
            # i번째 집을 안 털 경우: i-1까지의 최대값
            memo[n] = max(dp(n-2, memo) + nums[n], dp(n-1, memo))
            
            return memo[n]
        
        return dp(len(nums)-1)