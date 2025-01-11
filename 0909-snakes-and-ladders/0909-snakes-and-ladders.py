class Solution:
   def snakesAndLadders(self, board: List[List[int]]) -> int:
       from collections import deque
       n = len(board)

       # 2차원 보드를 1차원 배열로 변환
       # 아래에서 위로, 지그재그 패턴으로 변환
       arr = []
       for i in range(n-1, -1, -1):  # 아래 행부터 시작
           row = board[i]
           if (n-1-i) % 2 == 1:  # 홀수 행은 역순으로
               row = row[::-1]
           arr.extend(row)
       
       # BFS 초기화
       queue = deque([1])  # 시작점(1번 인덱스)
       visited = {1: 0}    # key: 위치, value: 이동 횟수

       while queue:
           curr = queue.popleft()  # 현재 위치
           
           # 목표 도달 확인 (n*n 인덱스가 마지막 칸)
           if curr == n*n:
               return visited[curr]
           
           # 주사위 굴리기 (1-6)
           for dice in range(1, 7):
               next_pos = curr + dice  # 주사위 굴려서 이동
               
               # 보드 범위 체크
               if next_pos > n*n:
                   continue

               destination = next_pos
               
               # 뱀/사다리가 있는지 확인
               if arr[next_pos-1] != -1:  # 뱀/사다리가 있는 경우
                   destination = arr[next_pos-1]
               
               # 방문하지 않은 칸이면 방문
               if destination not in visited:
                   visited[destination] = visited[curr] + 1  # 이동 횟수 증가
                   queue.append(destination)
                   
       return -1 