class Solution:
    def isValid(self, s: str) -> bool:
        """
        괄호의 짝이 맞는지 검사하는 함수
        stack을 이용해 여는 괄호는 넣고, 닫는 괄호를 만나면 짝이 맞는지 확인
        """
        # 문자열 길이가 1이면 무조건 짝이 맞지 않으므로 False 반환
        if len(s) == 1:
            return False
    
        # 괄호를 저장할 스택
        stack = []
        # 닫는 괄호를 key로, 해당하는 여는 괄호를 value로 하는 딕셔너리
        char = {')':'(', '}':'{', ']':'['}

        for c in s:
            # 스택이 비어있으면 현재 문자를 스택에 추가
            if not stack:
                stack.append(c)
            # 현재 문자가 여는 괄호면 스택에 추가
            # (char 딕셔너리의 key에 없는 문자 = 여는 괄호)
            elif c not in char:
                stack.append(c)
            # 현재 문자가 닫는 괄호인 경우
            elif c in char:
                # 스택의 top에 있는 괄호가 현재 닫는 괄호와 짝이 맞으면
                if char[c] == stack[-1]:
                    # 스택에서 제거 (짝이 맞는 여는 괄호 제거)
                    stack.pop()
                # 스택의 top에 있는 괄호가 현재 닫는 괄호와 짝이 맞지 않으면
                elif char[c] != stack[-1]:
                    # 유효하지 않은 괄호 문자열이므로 False 반환
                    return False
        
        # 모든 검사가 끝난 후
        # 스택이 비어있으면 True (모든 괄호의 짝이 맞음)
        # 스택에 괄호가 남아있으면 False (짝이 맞지 않는 괄호가 있음)
        return True if not stack else False