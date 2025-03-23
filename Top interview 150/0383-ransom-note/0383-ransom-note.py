class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        if len(ransomNote) > len(magazine):
            return False
        
        dict_note = Counter(ransomNote)
        dict_maga = Counter(magazine)

        for i, k in enumerate(dict_note):
            if dict_note[k] > dict_maga[k]:
                return False
        return True