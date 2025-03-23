class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:   # 오른쪽은 볼 필요 없음 (peak이 왼쪽에 있거나 mid가 peak)
                right = mid
            elif nums[mid] <= nums[mid+1]:  # 왼쪽은 볼 필요 없음 (peak이 오른쪽에 있음)
                left = mid + 1

        return left
            