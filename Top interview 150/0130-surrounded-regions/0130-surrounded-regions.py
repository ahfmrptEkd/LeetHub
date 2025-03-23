class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(x, y, n, m):
            return 0<=x<n and 0<=y<m
       
        def dfs(x,y): # DFS로 연결된 'O' 탐색
            if not valid(x,y,n,m) or board[x][y] != "O":
                return

            board[x][y] = "#" # 테두리와 연결된 'O' 임시 표시

            for i in range(4): # 4방향 탐색
                nx, ny = x + dx[i], y + dy[i]
                dfs(nx, ny)
            
        n, m = len(board), len(board[0])
        dx = [1,-1,0,0] # 상하좌우 이동 배열
        dy = [0,0,-1,1]

        # 테두리에서 시작하는 'O' 영역 찾아서 '#'로 표시
        for i in range(n):
            dfs(i, 0)    # 왼쪽 테두리
            dfs(i, m-1)  # 오른쪽 테두리
        for j in range(m):
            dfs(0, j)    # 위쪽 테두리
            dfs(n-1, j)  # 아래쪽 테두리

        # '#': 테두리와 연결된 'O' -> 'O'로 복원
        # 'O': 포위된 영역 -> 'X'로 변경
        for i in range(n):
            for j in range(m):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
            

