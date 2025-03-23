class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 두 배열의 전체 길이 계산
        total = len(nums1) + len(nums2)
        # 중앙값의 위치 계산 (0-인덱스 기준)
        mid = total // 2

        # 현재 값과 이전 값을 저장하는 변수 (중앙값 계산에 사용)
        prev = curr = 0
        # 현재까지 처리한 요소의 개수
        count = 0
        # 두 배열의 인덱스
        i = j = 0

        # 중앙값 위치까지 요소를 순회
        while count <= mid:
            # 현재 값을 이전 값으로 저장
            prev = curr

            # 두 배열 중 더 작은 값을 선택하여 현재 값으로 설정
            # nums1 배열을 모두 처리했거나, nums2의 현재 요소가 nums1의 현재 요소보다 작은 경우
            if i == len(nums1) or (j < len(nums2) and nums2[j] < nums1[i]):
                # nums2의 현재 요소를 선택
                curr = nums2[j]
                # nums2의 다음 요소로 이동
                j += 1
            else:
                # nums1의 현재 요소를 선택
                curr = nums1[i]
                # nums1의 다음 요소로 이동
                i += 1

            # 처리한 요소 개수 증가
            count += 1

        # 짝수 개수인 경우 중앙에 위치한 두 값의 평균을 반환
        if total % 2 == 0:
            return (prev + curr) / 2

        # 홀수 개수인 경우 중앙에 위치한 값을 반환
        return float(curr)
