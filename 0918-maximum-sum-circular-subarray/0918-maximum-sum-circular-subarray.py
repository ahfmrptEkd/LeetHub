class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """필요한 2가지!!
        기본 카데인과 원형 카데인 중 큰걸 반환 해야한다."""
        def kadane(arr):
            max_end = max_curr = arr[0]

            for i in arr[1:]:
                max_end = max(i, i+max_end)
                max_curr = max(max_curr, max_end)
            
            return max_curr
        
        # 1. 일반 카데인
        regular_max = kadane(nums)
        
        # 모든 원소 음수 일 때의 예외 처리
        if max(nums) <= 0:
            return regular_max

        # 2. 원형 배열의 카데인
        total = sum(nums)
        min_subarray = kadane([-n for n in nums])   # 음수의 최대 부분합 == 원래 배열의 최소 부분합

        # 최소 부분합을 제외한 나머지가 원형으로 연결 된 최대 부분합
        circular_max = total + min_subarray         # total + min_subarray == total - (-min_subarray)

        # 2개를 비교해서 큰걸 반환 하면 된다.
        return max(circular_max, regular_max)
