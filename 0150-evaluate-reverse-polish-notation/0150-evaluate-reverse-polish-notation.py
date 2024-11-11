class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        사칙연산 나오면 2개를 뽑고 a,b 연산 후 넣는거 반복.
        기호가 나오면 2번 빼서 순차적으로 b, a
        나온값을 append
        빌 때 까지 반복
        
        """
        stack = []
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }

        if len(tokens) == 1:
            return int(tokens[0])

        # print(operations['+'](1,2))

        for t in tokens:
            if t in operations:
                b = int(stack.pop())
                a = int(stack.pop())
                output = operations[t](a,b)
                stack.append(output)
            else:
                stack.append(t)

        return int(stack.pop())    