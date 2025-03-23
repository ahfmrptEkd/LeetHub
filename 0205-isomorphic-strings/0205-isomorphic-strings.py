class Solution:
   def isIsomorphic(self, s: str, t: str) -> bool:
       # match: 문자 간의 매핑을 저장하는 딕셔너리 (s -> t)
       match = {}
       # used: 이미 매핑된 대상 문자(t의 문자)들을 저장하는 집합
       used = set()

       # s와 t의 문자를 동시에 순회
       for k, v in zip(s, t):
           # 케이스 1: k이 아직 매핑되지 않은 문자인 경우
           if k not in match:
               # v가 이미 다른 문자에 매핑되어 있으면 False
               if v in used:
                   return False
               # 새로운 매핑 추가
               match[k] = v
               # 매핑된 문자(v)를 used 집합에 추가
               used.add(v)
           # 케이스 2: k이 이미 매핑된 문자인 경우
           elif match[k] != v:
               # 기존 매핑과 다른 문자가 오면 False
               return False
       
       # 모든 검사를 통과하면 동형 문자열임
       return True