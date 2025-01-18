class Trie():
    def __init__(self):
        self.children = {}      # 각 문자를 key로 하는 자식 노드들을 저장
        self.is_end = False     # 현재 노드가 단어의 끝인지 표시
        self.word = ""          # 현재 노드가 단어의 끝이라면, 여기에 전체 단어 저장

    def insert(self, word:str) -> None:    # 트라이에 단어 삽입
        curr = self
        for c in word:
            if c not in curr.children:      # 현재 문자에 대한 노드가 없으면 새로 생성
                curr.children[c] = Trie()
            curr = curr.children[c]         # 다음 문자로 이동
        curr.is_end = True                  # 단어의 끝 표시
        curr.word = word                    # 전체 단어 저장

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def is_valid(nx, ny) -> bool:       # 좌표가 보드 범위 내에 있는지 확인
            return (0 <= nx < n) and (0 <= ny < m)
        
        def dfs(x, y, trie):                # DFS로 보드를 탐색하며 단어 찾기
            if trie.is_end:                 # 현재 노드가 단어의 끝이면
                ans.add(trie.word)          # 결과 집합에 단어 추가
                trie.is_end = False         ## 찾은 단어 제거 (속도 향상)

            original = board[x][y]          # 현재 칸의 원래 값 저장
            board[x][y] = "#"              # 방문 표시

            # 4방향 탐색 (상하좌우)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]  # 다음 위치 계산
                if not is_valid(nx, ny):       # 보드 범위를 벗어나면 스킵
                    continue
                if board[nx][ny] == '#':       # 이미 방문한 칸이면 스킵
                    continue
                c = board[nx][ny]              # 다음 칸의 문자
                if c in trie.children:         # 해당 문자가 트라이에 있으면
                    dfs(nx,ny,trie.children[c]) # 계속 탐색
                    if not trie.children[c].children and not trie.children[c].is_end:   # 빈 dictionary이면서 단어 끝이 없다?
                        del trie.children[c]                                            # 노드 삭제 (속도 향상)
            board[x][y] = original            # 백트래킹: 원래 값으로 복구

        def combination():
            board_chars = set(ch for row in board for ch in row)

            filtered_words = []
            for word in words:
                if all(c in board_chars for c in word):
                    filtered_words.append(word)
            
            filtered_words.sort(key=len)
            return filtered_words

        filterd_words = combination()

        trie = Trie()                      # 트라이 생성
        for word in filterd_words:                 # 모든 단어를 트라이에 삽입
            trie.insert(word)

        n, m = len(board), len(board[0])    # 보드의 크기
        ans = set()                         # 찾은 단어들을 저장할 집합
        dx = [1, -1, 0, 0]                 # 상하좌우 이동을 위한 x방향 배열
        dy = [0, 0, 1, -1]                 # 상하좌우 이동을 위한 y방향 배열
        # 보드의 모든 칸에서 시작해보기
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie.children:  # 첫 문자가 트라이에 있으면
                    dfs(i,j,trie.children[board[i][j]])  # DFS 시작

        return list(ans)                    # 찾은 단어들을 리스트로 변환하여 반환