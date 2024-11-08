class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        merge = []

        for item in intervals:
            if not merge or merge[-1][1] < item[0]:
                merge.append(item)
            else:
                merge[-1][1] = max(merge[-1][1], item[1])

        return merge