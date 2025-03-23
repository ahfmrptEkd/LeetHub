class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, current_count, curr_combine):
            if current_count == k:
                result.append(curr_combine[:])  # [:] 사용하여 새로운 리스트를 생성 (참조가 아닌 값을 복사)
                return
            
            for i in range(start, n+1):
                curr_combine.append(i)
                backtrack(i+1, current_count + 1, curr_combine)
                curr_combine.pop()  # 백트래킹: 마지막에 추가한 숫자를 제거하여
        
        result = []
        # 백트래킹 시작 (1부터 시작, 선택한 숫자 0개, 빈 조합)
        backtrack(1, 0, [])
        return result
