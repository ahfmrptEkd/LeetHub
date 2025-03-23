import heapq as hp
class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.big = []   # min heap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.big):
            hp.heappush(self.small, -hp.heappushpop(self.big, num))
        else:
            hp.heappush(self.big, -hp.heappushpop(self.small, -num))

    def findMedian(self) -> float:
        if not self.small:
            return 0
        if len(self.small) > len(self.big):
            return -self.small[0]
        return (-self.small[0] + self.big[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()