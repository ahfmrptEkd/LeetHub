class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import copy
        # 현재 셀의 8방향 이웃을 찾기 위한 좌표 배열
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # 원본 보드의 복사본 생성
        copy_board = copy.deepcopy(board)

        # 보드의 모든 셀을 순회
        for row in range(rows):
            for col in range(cols):

                # 각 셀마다 살아있는 이웃의 수를 계산
                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # 이웃 셀이 보드 범위 내에 있는지 확인하고, 원래 살아있는 셀이었는지 확인
                    if (0 <= r < rows) and (0 <= c < cols) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # 규칙 1 & 규칙 3: 살아있는 셀이 이웃이 2개 미만이거나 3개 초과면 죽음        
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # 규칙 4: 죽은 셀이 정확히 3개의 살아있는 이웃을 가지면 살아남
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1