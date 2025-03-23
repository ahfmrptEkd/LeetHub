class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 이번에는 원소 한개만 지웠을 때의 가장 큰 1의 길이
        length = 0  # 길이
        count = 0 # 원소를 지운 개수
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0: # 0인 원소를 보면
                count += 1
                
            while count > 1: # 0를 2개이상 만나면 l을 올린다.
                if nums[l] == 0:
                    count -= 1
                l += 1

            length = max(length, r - l) 

            # 0이 없는 경우
            if r == len(nums) -1 and l == 0: # 마지막까지 순회해서  0이 없다면.
                return len(nums) - 1
          
        return length