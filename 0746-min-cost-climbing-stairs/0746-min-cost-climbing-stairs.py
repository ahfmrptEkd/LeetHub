class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(num):
            if num == 0:
                return 0
            if num == 1:
                return 0
            
            if num in memo:
                return memo[num]
            
            memo[num] =  min(dp(num-1) + cost[num - 1], dp(num-2) + cost[num - 2])

            return memo[num]
        
        memo = {}

        return dp(len(cost))  