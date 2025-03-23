class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 문제 조건:
        # 1. 정확히 하나의 유효한 답만 존재
        # 2. 같은 원소를 두 번 사용할 수 없음
        # 3. 답은 두 수의 인덱스를 담은 리스트로 반환
        
        # 해시맵(딕셔너리)를 사용하여 각 숫자의 인덱스를 저장
        past = {}
        
        # 리스트를 한 번만 순회하면서 답을 찾음 (O(n) 시간 복잡도)
        for i, num in enumerate(nums):
            # 현재 숫자와 더해서 target이 되는 수(complement) 계산
            complement = target - num
            
            # complement가 이미 past에 있다면 답을 찾은 것
            if complement in past:
                # [이전에 저장된 complement의 인덱스, 현재 숫자의 인덱스] 반환
                return [past[complement], i]
            
            # 현재 숫자와 그 인덱스를 past에 저장
            # 다음 순회에서 다른 숫자의 complement로 활용될 수 있음
            past[num] = i
