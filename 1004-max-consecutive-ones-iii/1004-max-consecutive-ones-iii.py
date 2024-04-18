class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = 0 # 1의 숫자를 업데이트할 수
        count = 0   # 0을 셀 카운트
        l, r = 0, 0

        # 투포인터 또한 슬라이딩의 기법중 하나가 될 수 있다.
        while r < len(nums):
            if nums[r] == 0:
                count += 1

            while count > k:    # 0의 수가 k의 범위를 넘어가면
                if nums[l] == 0:  # 그만큼 없을 때 까지 넘어가야함.
                    count -= 1
                l += 1  # 윈도우 크기 감소
            
            length = max(length, r - l + 1)
            r += 1
        
        return length
                    




