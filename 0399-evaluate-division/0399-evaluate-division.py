class Solution:
   def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
       # 형태: {'변수': [(연결된변수, 나눗셈값), ...]}
       graph = {}

       # equations와 values를 순회하며 그래프 구성
       # zip으로 [["a","b"], ["b","c"]]와 [2.0, 3.0]를 동시에 순회
       for (x, y), val in zip(equations, values):
           # 처음 보는 변수라면 빈 리스트로 초기화
           if x not in graph:
               graph[x] = []
           if y not in graph:
               graph[y] = []    
           # x/y = val 관계 저장
           graph[x].append((y, val))
           # y/x = 1/val 관계도 저장 (역방향 엣지)
           graph[y].append((x, 1/val))
       
       def dfs(start, end, visited):
           # start 노드가 그래프에 없으면 계산 불가능
           if start not in graph:
               return -1.0
           # 시작점이 도착점과 같으면 나누기 결과는 1
           if start == end:
               return 1.0
           
           # 현재 노드 방문 처리
           visited.add(start)

           # 현재 노드와 연결된 모든 노드들 탐색
           for next_node, val in graph[start]:
               # 방문하지 않은 노드에 대해서만
               if next_node not in visited:
                   # 다음 노드부터 목표까지의 경로 탐색
                   result = dfs(next_node, end, visited)
                   # 경로를 찾았다면 현재 간선의 값과 곱해서 반환
                   if result != -1.0:
                       return result * val
           # 모든 경로를 탐색했는데 목표를 못 찾으면 -1.0 반환
           return -1.0
       
       # 각 쿼리에 대해 DFS 실행
       # set()으로 매번 새로운 방문 기록 세트 생성
       return [dfs(start, end, set()) for start, end in queries]
