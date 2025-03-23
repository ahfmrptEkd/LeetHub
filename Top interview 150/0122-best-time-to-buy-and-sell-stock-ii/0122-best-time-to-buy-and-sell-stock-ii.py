class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0

        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                total += prices[i] - prices[i-1]
            else:
                continue
        return total
