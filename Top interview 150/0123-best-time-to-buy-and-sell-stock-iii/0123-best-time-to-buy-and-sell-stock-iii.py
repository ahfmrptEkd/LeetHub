class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 가격 배열의 길이가 2 미만이면 거래할 수 없으므로 0 반환
        if len(prices) < 2:
            return 0
        
        # 주식 가격 배열의 길이
        n = len(prices)
        # DP 테이블 초기화: dp[i][k]는 i일까지 최대 k번 거래했을 때의 최대 이익
        # k=0은 거래 없음, k=1은 첫 번째 거래까지의 최대 이익, k=2는 두 번째 거래까지의 최대 이익
        dp = [[0] * 3 for _ in range(n)]
        print(dp)
        
        # 각 거래 횟수(k)에 대해 반복
        for k in range(1, 3):
            # max_difference는 "(k-1)번째 거래까지의 최대 이익 - 현재 주식 가격"의 최대값
            # 첫날에는 주식을 사는 경우만 고려하므로 -prices[0]로 초기화
            max_difference = -prices[0]

            # 1일차부터 마지막 날까지 각 날짜에 대한 최대 이익 계산
            for i in range(n):
                # 두 가지 선택 중 최대값:
                # 1) 오늘 아무것도 안 하고 이전 날의 상태 유지 (dp[i-1][k])
                # 2) 오늘 주식을 판매 (prices[i] + max_difference)
                dp[i][k] = max(dp[i-1][k], prices[i] + max_difference)

                # max_difference 갱신: 
                # "k-1번째 거래까지의 최대 이익 - 현재 주식 가격"과 현재 max_difference 중 큰 값
                # 이는 "이전 거래의 이익을 유지하면서 현재 가격에 주식을 살 때 남는 돈"의 최대값
                max_difference = max(max_difference, dp[i][k-1] - prices[i])
        
        # 마지막 날까지 최대 2번 거래했을 때의 최대 이익 반환
        return dp[n-1][2]