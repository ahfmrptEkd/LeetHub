class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        최적의 해결책은 Boyer-Moore 과반수 투표 알고리즘을 사용하는 것입니다. 이 알고리즘은 O(n) 시간 복잡도와 O(1) 공간 복잡도를 가지며
        문제에서 "과반수 원소가 항상 존재한다"고 가정했으므로, 이 알고리즘은 항상 정확한 결과를 반환합니다
        """
        candidate = None
        count = 0
        # nums.sort()   # 이 부분이 있든 없든 항상 정확하다.
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate