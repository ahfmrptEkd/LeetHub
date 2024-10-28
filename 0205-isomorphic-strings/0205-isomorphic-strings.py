class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        match = {}
        used = set()

        for c1, c2 in zip(s, t):
            if c1 not in match:
                if c2 in used:
                    return False
                match[c1] = c2
                used.add(c2)
            elif match[c1] != c2:
                return False
        return True