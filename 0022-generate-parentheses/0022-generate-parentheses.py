class Solution:
   def generateParenthesis(self, n: int) -> List[str]:
       def backtrack(open_count, close_count, combination):
           # 현재 조합의 길이가 2n이면 유효한 괄호 조합이므로 결과에 추가
           if len(combination) == n*2:
               result.append(combination)
               return
           
           # 열린 괄호의 개수가 n보다 작으면 열린 괄호 추가 가능
           if open_count < n:
               backtrack(open_count+1, close_count, combination + "(")
           
           # 닫힌 괄호의 개수가 열린 괄호보다 작으면 닫힌 괄호 추가 가능
           if close_count < open_count:
               backtrack(open_count, close_count+1, combination + ")")

       result = []  # 결과를 저장할 리스트
       backtrack(0, 0, "")  # 백트래킹 시작 (열린 괄호 0개, 닫힌 괄호 0개, 빈 문자열)

       return result