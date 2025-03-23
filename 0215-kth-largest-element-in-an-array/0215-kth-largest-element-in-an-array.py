class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as hp

        # 모든 원소를 한번에 음수로 변환
        nums = [-n for n in nums]

        # heap으로 변환: O(n)
        hp.heapify(nums)

        # k번 pop: O(k log n)
        for i in range(k-1):
            hp.heappop(nums)
        
        return -hp.heappop(nums)