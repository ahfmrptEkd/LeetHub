class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: return 1    # 문자열이 1개인 경우.

        ans = 0
        i = 0

        while i < len(chars): # 중복 개수 값은 전체 문자열보다 작거나 같다.
            letter = chars[i]
            count = 0

            while i < len(chars) and chars[i] == letter: # i는 배열의 길이 안에 있으면서, 문자열이 같은 곳까지 샌다.
                count += 1
                i += 1
            
            chars[ans] = letter # 한개 문자를 확정
            ans += 1    # 문자열 개수를 증가

            if count > 1:   # 2개이상인 경우부터는 숫자를 리스트에 넣고 길이가 길어짐.
                for s in str(count):
                    chars[ans] = s
                    ans += 1
        
        return ans