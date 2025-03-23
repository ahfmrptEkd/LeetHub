class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ']':
                decoded_string = ""
                # 인코딩된 문자열 추출
                while stack and stack[-1] != '[':
                    decoded_string = stack.pop() + decoded_string
                stack.pop()  # '[' 제거
                base = 1
                k = 0
                # 숫자 k 추출
                while stack and stack[-1].isdigit():
                    k = k + int(stack.pop()) * base
                    base *= 10
                # k[decodedString] 디코딩, 스택에 decodedString을 k번 푸시
                decoded_string *= k
                for char in decoded_string:
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack)