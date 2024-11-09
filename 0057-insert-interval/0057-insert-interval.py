class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key= lambda x: x[0])
        merge = []

        for item in intervals:
            if not merge or (merge[-1][1] < item[0]):
                merge.append(item)
            else:
                merge[-1][1] = max(merge[-1][1], item[1])
        return merge