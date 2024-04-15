class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u',"A","E","I","O","U"]
        l = 0
        r = len(s) - 1
        w = [0] * len(s)  # 리스트 초기화

        while l <= r:
            # 포인터는 스위칭이 아닌 줄거나 늘어나기만 해야함.    
            if s[l] not in vowels: # 모음이 아닌 경우 -> 패스
                w[l] = s[l]
                l += 1 # l만 넣고 올림
            
            # l만 모음인 경우 (1)
            elif s[r] not in vowels:
                w[r] = s[r]
                r -= 1 # r만 넣고 내림
            
            # 둘다 모음인 경우 (2) 
            else:
                w[l], w[r] = s[r], s[l]
                l += 1
                r -= 1

        result = ''.join(w)
        return result
