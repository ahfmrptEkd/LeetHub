class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:  # 왼쪽이 정렬되어 있는 부분

                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
            else:                       # 오른쪽이 정렬되어 있는 부분
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1