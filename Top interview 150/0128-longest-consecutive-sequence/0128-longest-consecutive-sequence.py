class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 순차적인걸 찾아야함
        # 순차적인게 가장 큰 길이를 return 하면 됌.
        streak = 0
        dict_num = set(nums)
        
        for n in nums:
            if n -1 not in dict_num:
                current = n 
                current_streak = 1

                while current + 1 in dict_num:
                    current += 1
                    current_streak += 1
                
                streak = max(streak, current_streak)
        
        return streak