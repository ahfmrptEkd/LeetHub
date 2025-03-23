class Solution:
    def reverseWords(self, s: str) -> str:
        import re # split 함수 대신 re.split으로 정규표현식으로 제거

        c = re.split(r'\s+', s.strip()) # \s+는 하나 이상의 공백을 의미      
        l = 0
        r = len(c) - 1


        while l < r:
            c[l], c[r] = c[r], c[l]
            l += 1
            r -= 1
        
        result = ' '.join(c)
        return result