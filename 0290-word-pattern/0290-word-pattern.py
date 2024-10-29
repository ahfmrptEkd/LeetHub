from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = list(s.split())
        match = defaultdict(str)
        rev = defaultdict(str)
        # used = set()

        if len(pattern) != len(word):
            return False

        for c, w in zip(pattern, word):
            if c not in match:
                if w in rev:
                    if rev[w] != c:
                        return False
                match[c] = w
                rev[w] = c
            elif match[c] != w:
                    return False
        return True