from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(m, n):
            if len(word) > m * n:
                return False
            
            board_counter = Counter()
            for i in range(m):
                for j in range(n):
                    board_counter[board[i][j]] += 1
            
            word_counter = Counter(word)
            for ch, count in word_counter.items():
                if count > board_counter[ch]:
                    return False
            return True

        
        def backtrack(x: int, y: int, idx: int) -> bool:
        # def backtrack(x: int, y: int, idx: int, container: list) -> bool:
            # 단어를 모두 찾았으면 성공
            if idx == len(word):
                return True
            
            # 상하좌우 네 방향 탐색
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                
                # 새로운 위치가 유효하고 아직 방문하지 않은 칸인 경우
                if 0<= nx < m and 0<= ny < n and not visited[nx][ny] and board[nx][ny] == word[idx]:
                    
                    # 현재 위치의 문자가 찾는 문자와 일치하는 경우
                    visited[nx][ny] = True
                    
                    # 다음 문자를 찾기 위해 재귀 호출
                    # 성공한 경로를 찾으면 즉시 True 반환
                    if backtrack(nx, ny, idx + 1):
                        return True

                    # 실패한 경로는 백트래킹
                    visited[nx][ny] = False

            return False

        # 보드의 크기 저장
        m, n = len(board), len(board[0])
        
        if not check(m,n):
            return False
        
        # 방문 여부를 추적하는 2차원 배열
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        # 보드의 모든 위치에서 시작해보기
        for i in range(m):
            for j in range(n):
                letter = board[i][j]
                # 시작 위치의 글자가 찾는 단어의 첫 글자와 일치하는 경우만 탐색 시작
                if letter == word[0]:
                    visited[i][j] = True
                    if backtrack(i, j, 1):
                        return True
                    visited[i][j] = False  # 실패시 백트래킹

        return False  # 모든 시작점에서 실패한 경우