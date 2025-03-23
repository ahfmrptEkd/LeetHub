class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        text = s.strip().split()
        target = text[-1]

        return len(target)