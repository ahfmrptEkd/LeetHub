class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(used, combination):
            if len(combination) == len(nums):
                result.append(combination[:])  # 현재 조합을 결과에 추가
                return
            
            # 모든 숫자에 대해 시도
            for i in range(len(nums)):
                # 아직 사용하지 않은 숫자라면
                if not used[i]:
                    used[i] = True  # 사용했다고 표시
                    combination.append(nums[i])  # 현재 조합에 추가
                    backtrack(used, combination)  # 다음 숫자 선택하러 재귀 호출
                    combination.pop()  # 백트래킹: 현재 숫자 제거
                    used[i] = False  # 사용하지 않았다고 다시 표시
        
        if len(nums) == 1:
            return [nums]

        used = [False] * len(nums)
        result = []  # 모든 순열을 저장할 리스트
        backtrack(used, [])  # used 배열과 빈 조합으로 시작
        return result