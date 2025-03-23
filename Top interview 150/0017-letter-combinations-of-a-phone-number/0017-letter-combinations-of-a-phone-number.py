class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(i, current):
            # 기저 조건: 현재 인덱스가 digits의 길이와 같을 때 (모든 숫자를 처리했을 때)
            if i == len(digits):
                result.append(current)
                return
            
            # 현재 처리할 숫자를 가져옴
            digit = digits[i]
            # 현재 숫자에 매핑되는 모든 문자에 대해 재귀 호출
            for letter in d2l[digit]:
                # 현재 문자를 조합에 추가하고 다음 인덱스로 진행
                backtrack(i+1, current + letter)
        
        # 빈 문자열 처리
        if len(digits) == 0:
            return []

        # 숫자-문자 매핑 딕셔너리
        d2l = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []  # 결과를 저장할 리스트
        backtrack(0, "")  # 백트래킹 시작 (인덱스 0, 빈 문자열부터)

        return result