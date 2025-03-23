class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        사칙연산 나오면 2개를 뽑고 a,b 연산 후 넣는거 반복.
        기호가 나오면 2번 빼서 순차적으로 b, a
        나온값을 append
        빌 때 까지 반복
        
        """
        # 계산 과정에서 숫자를 저장할 스택
        stack = []
        
        # 연산자와 그에 대응하는 람다 함수를 딕셔너리로 정의
        operations = {
            '+': lambda x, y: x + y,  # 덧셈 연산
            '-': lambda x, y: x - y,  # 뺄셈 연산
            '*': lambda x, y: x * y,  # 곱셈 연산
            '/': lambda x, y: x / y   # 나눗셈 연산
        }

        # 토큰이 하나만 있는 경우 (단일 숫자인 경우)
        if len(tokens) == 1:
            return int(tokens[0])

        # 토큰을 하나씩 처리
        for t in tokens:
            # 현재 토큰이 연산자인 경우
            if t in operations:
                # 스택에서 두 개의 숫자를 꺼냄 (순서 주의: 나중에 들어간 것이 두 번째 피연산자)
                b = int(stack.pop())  # 두 번째 피연산자
                a = int(stack.pop())  # 첫 번째 피연산자
                
                # 해당 연산을 수행하고 결과를 스택에 추가
                output = operations[t](a,b)
                stack.append(output)
            # 현재 토큰이 숫자인 경우
            else:
                # 스택에 숫자를 추가
                stack.append(t)

        # 최종 결과 반환 (정수형으로 변환)
        return int(stack.pop())