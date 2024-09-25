class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        local_min = prices[0]
        local_max = prices[0]
        total = 0

        for i in range(len(prices)):
            
            if prices[i] < local_max:
                print("sold")
                total += local_max - local_min
                print(f"total: {total}")    
                local_min = prices[i]
                local_max = prices[i]
                print(f"local_min: {local_min}")
            else:
                local_max = prices[i]
                print(f"local_max: {local_max}")
        total += local_max - local_min
        return total