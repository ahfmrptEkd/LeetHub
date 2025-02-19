class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        if nums[left] < nums[right]:
            return nums[left]

        while left <= right:
            mid = (left + right) // 2

            # 중간값이 이전 값보다 작으면 그게 최솟값
            if 0 < mid and nums[mid - 1] > nums[mid] :
                return nums[mid]

            # 다음 값이 현재 값보다 작으면 그게 최솟값
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # 왼쪽이 정렬되어 있으면 오른쪽 탐색
            elif nums[left] < nums[mid]:
                left = mid + 1
                
            # 오른쪽이 정렬되어 있으면 왼쪽 탐색
            else:
                right = mid - 1