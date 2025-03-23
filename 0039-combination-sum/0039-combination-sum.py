class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 타겟이 1인 경우는 문제의 제약조건에 따라 빈 리스트 반환
        if target == 1:
            return []

        def backtrack(start, container):
            # 현재 조합의 합이 타겟과 일치하면 결과에 추가
            if sum(container) == target:
                result.append(container[:])  # [:] 사용하여 깊은 복사
                return
            # 현재 조합의 합이 타겟보다 크면 더 이상 진행하지 않음
            elif sum(container) > target:
                return
            
            # start부터 시작하여 candidates를 순회
            # start부터 시작함으로써 이전 숫자는 고려하지 않아 중복 조합 방지
            for i in range(start, n):
                container.append(candidates[i])  # 현재 숫자 추가
                backtrack(i, container)  # 같은 숫자를 또 사용할 수 있으므로 i부터 시작
                container.pop()  # 백트래킹: 추가한 숫자 제거

        n = len(candidates)
        result = []
        backtrack(0, [])    # 백트래킹 시작 (시작 인덱스 0, 빈 컨테이너로 시작)

        return result