class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1. 1개의 숫자를 미리 잡아놓으면, 2sum  문제가 됨.
        """
        result = []  # 인덱스를 저장할 리스트
        nums.sort()
        print(nums)
        
        # 첫번째 i 선택
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                target = nums[i] + nums[l] + nums[r]

                if target < 0: #셋의 합이 0 보다 작으면 l 증가
                    l += 1
                elif target > 0: #셋의 합이 0 보다 크면 r 감소
                    r -= 1
                else:       # 0 인 경우
                    result.append([nums[i], nums[l], nums[r]])

                    # 중복값 건너뛰기
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
        
        return result
