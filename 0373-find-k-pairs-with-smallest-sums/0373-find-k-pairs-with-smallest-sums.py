class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq as hp

        heap = []
        result = []

        # k와 nums1 길이 중 작은 값만큼만 초기화 (불필요한 조합 방지) & nums1 와 nums2의 첫번째 원소 조합 초기화
        for i in range(min(k, len(nums1))):
            hp.heappush(heap, [nums1[i] + nums2[0], i, 0])

        # 힙이 비어있지 않고, k개를 아직 못 찾았다면 계속 진행
        while heap and len(result) < k:
            _, i, j = hp.heappop(heap)  # 현재 가장 작은 합을 가진 쌍을 꺼냄
            result.append([nums1[i], nums2[j]]) # 결과 리스트에 쌍 추가

            # nums2에 다음 원소가 있다면 새로운 조합을 힙에 추가
            if j + 1 < len(nums2):
                hp.heappush(heap, [nums1[i] + nums2[j+1], i, j+1])
        
        return result