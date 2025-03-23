class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        싼 가격에 사서 비싼 가격에 판다.
        한 번의 순회로 최소 가격과 최대 이익을 추적하는 것.
        """
        max_profit = 0
        min_p = float('inf')
        
        if not prices:
            return 0

        for p in prices:
            if p < min_p:
                min_p = p
            else:
                max_profit = max(max_profit, p-min_p)
        
        return max_profit