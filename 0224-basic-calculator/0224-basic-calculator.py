class Solution:
   def calculate(self, s: str) -> int:
       """
       문자열로 된 수식을 계산하는 함수
       입력 문자열은 숫자, +, -, (, ), 공백으로 구성됨
       괄호가 포함된 수식을 재귀적으로 계산
       """
       def update(stack, num, oper):
           """
           스택에 숫자를 추가하는 함수
           
           Args:
               stack (list): 숫자들을 저장하는 스택
               num (int): 추가할 숫자
               oper (str): 현재 연산자 (+/-)
           """
           if oper == '+':
               stack.append(num)  # 양수는 그대로 추가
           elif oper == '-':
               stack.append(-num)  # 음수는 부호를 바꿔서 추가
       
       def calc(idx):
           """
           주어진 인덱스부터 수식을 계산하는 재귀 함수
           
           Args:
               idx (int): 현재 처리할 문자의 인덱스
               
           Returns:
               tuple: (계산 결과, 다음에 처리할 인덱스)
           """
           stack = []  # 숫자들을 저장할 스택
           num = 0     # 현재 만들고 있는 숫자
           operator = '+'  # 현재 연산자 (기본값 +)
           
           while idx < len(s):
               item = s[idx]
               
               if item.isdigit():
                   # 숫자인 경우 자릿수 계산
                   num = num * 10 + int(item)
               
               elif item == '(':
                   # 여는 괄호를 만나면 재귀적으로 괄호 안을 계산
                   num, next_idx = calc(idx + 1)
                   idx = next_idx  # 괄호 안의 계산이 끝난 위치로 인덱스 이동
               
               elif item == ')':
                   # 닫는 괄호를 만나면 현재까지의 계산 결과를 반환
                   update(stack, num, operator)
                   return sum(stack), idx
               
               if (not item.isdigit() and item != ' ') or idx == len(s) - 1:
                   # 연산자를 만나거나 문자열 끝에 도달했을 때
                   update(stack, num, operator)  # 현재까지의 숫자를 스택에 추가
                   operator = item  # 다음 연산을 위해 연산자 업데이트
                   num = 0  # 새로운 숫자를 위해 초기화
               
               idx += 1
           
           return sum(stack), idx  # 최종 계산 결과와 인덱스 반환

       # 한 자리 숫자인 경우 바로 반환
       if len(s) == 1:
           return int(s[0])

       # 공백 제거
       container = [x for x in s if x != " "]

       # 계산 시작
       res, _ = calc(0)
       return res