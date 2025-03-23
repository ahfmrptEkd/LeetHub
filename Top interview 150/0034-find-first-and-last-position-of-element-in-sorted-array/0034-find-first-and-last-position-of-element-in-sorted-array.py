class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # 가장 왼쪽의 target 위치를 찾는 함수
        def left_index():
            left, right = 0, len(nums) - 1
            first_pos = -1  # target을 못 찾을 경우를 대비해 -1로 초기화

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    first_pos = mid      # 현재 위치 저장
                    right = mid - 1      # 더 왼쪽에 있는 target을 찾기 위해 왼쪽 부분 탐색
                
                elif nums[mid] < target:  # 중간값이 target보다 작으면
                    left = mid + 1       # 오른쪽 부분 탐색
                
                else:                    # 중간값이 target보다 크면
                    right = mid - 1      # 왼쪽 부분 탐색
            
            return first_pos
        
        # 가장 오른쪽의 target 위치를 찾는 함수
        def right_index():
            left, right = 0, len(nums) - 1
            second_pos = -1  # target을 못 찾을 경우를 대비해 -1로 초기화

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    second_pos = mid     # 현재 위치 저장
                    left = mid + 1       # 더 오른쪽에 있는 target을 찾기 위해 오른쪽 부분 탐색
                
                elif nums[mid] < target:  # 중간값이 target보다 작으면
                    left = mid + 1       # 오른쪽 부분 탐색
                
                else:                    # 중간값이 target보다 크면
                    right = mid - 1      # 왼쪽 부분 탐색
            
            return second_pos

        # 빈 배열인 경우 바로 [-1, -1] 반환
        if not nums:
            return [-1, -1]
        
        # 가장 왼쪽 target 위치 찾기
        first = left_index()
        if first == -1:  # target이 배열에 없는 경우
            return [-1, -1]
        
        # 가장 오른쪽 target 위치 찾기
        second = right_index()

        return [first, second]  # 시작과 끝 위치 반환