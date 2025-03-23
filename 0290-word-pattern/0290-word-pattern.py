from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 문장 s를 공백을 기준으로 단어 리스트로 분리
        word = list(s.split())

        # 패턴 문자 -> 단어 매핑을 저장할 딕셔너리
        match = defaultdict(str)
        # 단어 -> 패턴 문자 매핑을 저장할 딕셔너리 (역방향 검증용)
        rev = defaultdict(str)

        # 패턴의 길이와 단어 리스트의 길이가 다르면 패턴이 일치할 수 없음
        if len(pattern) != len(word):
            return False

        # 패턴의 각 문자와 단어 리스트의 각 단어를 함께 순회
        for c, w in zip(pattern, word):
            # 현재 패턴 문자가 아직 매핑되지 않은 경우
            if c not in match:
                # 현재 단어가 이미 다른 패턴 문자에 매핑되어 있는지 확인
                if w in rev:
                    # 만약 현재 단어가 다른 패턴 문자에 매핑되어 있다면 패턴 불일치
                    if rev[w] != c:
                        return False
                # 새로운 매핑 관계 저장 (양방향)
                match[c] = w
                rev[w] = c
            # 현재 패턴 문자가 이미 매핑되어 있는 경우, 매핑된 단어와 현재 단어가 일치하는지 확인
            elif match[c] != w:
                # 매핑된 단어와 현재 단어가 다르면 패턴 불일치
                return False
        # 모든 검사를 통과하면 패턴이 일치함
        return True
