class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as hp

        heap = []
        for n in nums:
            hp.heappush(heap, -n)

        for i in range(k):
            max = -hp.heappop(heap)
        return max