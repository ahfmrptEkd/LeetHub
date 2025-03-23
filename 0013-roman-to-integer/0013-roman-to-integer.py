class Solution:
    def romanToInt(self, s: str):
        from collections import deque
        math = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        ans = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in math: # 인덱싱 범위를 넘지 않고 2개를 확인했을 때 있는 경우
                ans += math[s[i:i+2]]
                i += 2
            else:
                ans += math[s[i]]   # 아닌 나머지 동일하다는 뜻
                i += 1
        return ans