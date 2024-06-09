class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first = set()  # 1번 꺼 저장할 것.
        second = set() # 2번 꺼 저장할 것.

        for i in nums1:
            if i not in nums2:
                first.add(i)
        
        for j in nums2:
            if j not in nums1:
                second.add(j)
        
        return [first, second]
 