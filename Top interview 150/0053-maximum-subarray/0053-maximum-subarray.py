class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Kadane's Algorithm은 배열에서 최대 연속 부분합(maximum subarray sum)을 O(n) 시간에 찾는 동적 프로그래밍 알고리즘"""
        max_end = max_curr = nums[0]
        # print(f"init:{max_end, max_curr}")

        for n in nums[1:]:
            # print(f"n = {n}")
            max_end = max(n, n + max_end)
            max_curr = max(max_curr, max_end)
            # print(f"max_end:{max_end}, max_curr:{max_curr} \n")

        return max_curr