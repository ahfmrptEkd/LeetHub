from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # k 가 없으면 false
        # k 의 개수가 달라도 false
        # 둘의 길이가 달라도 false
        if len(s) != len(t):
            return False

        dict_s = Counter(s)
        dict_t = Counter(t)

        for k in dict_s:
            if k not in dict_t:
                return False
            elif dict_s[k] != dict_t[k]:
                return False
        return True