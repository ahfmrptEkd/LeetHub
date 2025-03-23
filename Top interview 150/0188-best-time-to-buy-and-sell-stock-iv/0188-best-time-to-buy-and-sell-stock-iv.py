class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [ [0] * (k + 1) for _ in range(n)]

        for t in range(1, k + 1):
            # 현재 잔고
            max_diff = -prices[0]
            for i in range(n):
                # 2가지 안팔거나(유지) or 파는 것 
                dp[i][t] = max(dp[i - 1][t], prices[i] + max_diff)
                
                # 현재 잔고와 이전 거래 횟수와 현재 가격을 팔 때의 잔고
                max_diff = max(max_diff, dp[i][t - 1] - prices[i] )
        return dp[-1][-1]