class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 중복값 둘의 원소 와 인덱스 찾기
        # 찾는건 index() 로 왼쪽걸 찾으면 될 듯.
        # 그 값이 k 보다는 작거나 같아야함.
        # dictionary 로 관리
        if len(nums) == 1:
            return False
    
        container = dict()
        
        for i, n in enumerate(nums):
            if n not in container:
                container[n] = i
            else:
                if (i - container[n]) <= k:
                    return True
                container[n] = i

        return False