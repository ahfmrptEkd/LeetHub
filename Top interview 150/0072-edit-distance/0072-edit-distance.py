class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        최적화된 편집 거리(Edit Distance) 알고리즘 구현
        
        시간 복잡도: O(m*n), 여기서 m은 word1의 길이, n은 word2의 길이
        공간 복잡도: O(min(m,n)), 더 짧은 문자열 길이만큼의 공간만 사용
        """
        # 특수 케이스 처리: 빈 문자열
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
            
        # 항상 짧은 문자열을 word2로 설정하여 메모리 사용 최적화
        if len(word1) < len(word2):
            word1, word2 = word2, word1
            
        # 이전 행과 현재 행만 저장하는 1D 배열 사용
        previous_row = list(range(len(word2) + 1))
        current_row = [0] * (len(word2) + 1)
        
        for i in range(1, len(word1) + 1):
            # 현재 행의 첫 번째 요소는 이전 행의 첫 번째 요소 + 1
            current_row[0] = i
            
            for j in range(1, len(word2) + 1):
                # 현재 비교하는 문자가 같은 경우, 편집 불필요
                if word1[i-1] == word2[j-1]:
                    current_row[j] = previous_row[j-1]
                else:
                    # 세 가지 편집 연산 중 최소값 선택
                    current_row[j] = min(
                        current_row[j-1] + 1,  # 삽입
                        previous_row[j] + 1,   # 삭제
                        previous_row[j-1] + 1  # 대체
                    )
            
            # 다음 반복을 위해 행 업데이트
            previous_row, current_row = current_row, previous_row
            
        # 마지막 행이 previous_row에 있으므로 해당 행의 마지막 요소가 결과
        return previous_row[len(word2)]