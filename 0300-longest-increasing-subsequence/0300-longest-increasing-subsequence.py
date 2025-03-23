class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        i = i번째로 끝나는 수열 중 가장 긴 부분 수열의길이
        """
        from bisect import bisect_left

        # def binary_search(arr, target):
        #     left, right = 0, len(arr)-1
            
        #     while left <= right:
        #         mid = (left+right) // 2
                
        #         if arr[mid] >= target:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     return left

        # dp 자체를 바꾸는 방식 (기존에 하던게 아님)
        dp = []

        for num in nums:
            pos = bisect_left(dp, num)
            # pos = binary_search(dp, num)

            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
        
        return len(dp)