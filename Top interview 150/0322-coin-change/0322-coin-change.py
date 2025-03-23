class Solution:
   def coinChange(self, coins: List[int], amount: int) -> int:
       # dp 배열을 amount + 1로 초기화 (amount + 1은 불가능한 값으로 사용)
       # dp[i]는 금액 i를 만들기 위한 최소 동전 개수를 저장
       dp = [amount + 1] * (amount + 1)
       
       # 금액 0을 만드는데 필요한 동전 개수는 0개
       dp[0] = 0

       # 1부터 목표 금액까지 각각의 금액에 대해 계산
       for i in range(1, amount+1):
           # 각 동전에 대해 반복
           for c in coins:
               # 현재 동전이 현재 금액보다 작거나 같은 경우에만 사용 가능
               if c <= i:
                   # dp[i]: 현재까지의 최소 동전 개수
                   # dp[i - c] + 1: 현재 동전을 사용했을 때의 동전 개수
                   # 둘 중 더 작은 값을 선택
                   dp[i] = min(dp[i], dp[i - c] + 1)
       
       # dp[amount]가 초기값(amount + 1)과 같다면 불가능한 경우이므로 -1 반환
       # 그렇지 않다면 dp[amount] 반환
       return dp[amount] if dp[amount] != amount + 1 else -1