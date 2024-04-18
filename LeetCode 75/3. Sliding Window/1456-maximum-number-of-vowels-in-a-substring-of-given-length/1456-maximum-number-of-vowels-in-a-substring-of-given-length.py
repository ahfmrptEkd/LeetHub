class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        currnt = 0
        
        vowels = "aeiou"

        for i in range(len(s)):
            if i >= k:          # 나가는 원소 확인
                if s[i-k] in vowels:
                    currnt -= 1
            
            if s[i] in vowels:  # i 가 커지기 전까지 윈도우를 확인
                currnt += 1
            
            res = max(currnt, res)
        return res