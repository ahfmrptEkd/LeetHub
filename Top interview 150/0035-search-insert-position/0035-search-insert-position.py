class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 탐색 범위의 시작점과 끝점을 초기화
        l, r = 0, len(nums) - 1

        # 왼쪽 포인터가 오른쪽 포인터보다 커질 때까지 반복
        while l <= r:
            # 중간 지점 계산
            mid = (l+r) // 2

            # target을 찾았다면 해당 인덱스 반환
            if nums[mid] == target:
                return mid
            # 중간값이 target보다 작으면 왼쪽 포인터를 중간 다음 위치로 이동
            elif nums[mid] < target:
                l = mid + 1
            # 중간값이 target보다 크면 오른쪽 포인터를 중간 이전 위치로 이동
            else:
                r = mid - 1
        
        # target을 찾지 못했다면 target이 들어갈 위치(l) 반환
        return l