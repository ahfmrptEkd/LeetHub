from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 두 문자열의 길이가 다르면 애너그램이 될 수 없으므로 False 반환
        if len(s) != len(t):
            return False

        # Counter를 사용해 각 문자열의 문자 빈도수를 딕셔너리로 변환
        # 예: 'hello' -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        dict_s = Counter(s)
        dict_t = Counter(t)

        # s의 각 문자에 대해
        for k in dict_s:
            # 해당 문자가 t에 없으면 애너그램이 아님
            if k not in dict_t:
                return False
            # 해당 문자의 빈도수가 다르면 애너그램이 아님
            elif dict_s[k] != dict_t[k]:
                return False
        
        # 모든 검사를 통과하면 애너그램임
        return True