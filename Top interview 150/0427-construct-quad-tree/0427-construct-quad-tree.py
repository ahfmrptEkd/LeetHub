"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(n, row, col):
            # 현재 그리드가 모두 같은 값인지 확인
            all_same = True
            val = grid[row][col]  # 첫 번째 값을 기준값으로 설정
            
            # 현재 부분 그리드의 모든 값이 같은지 확인하는 이중 루프
            for i in range(row, row + n):
                for j in range(col, col + n):
                    if grid[i][j] != val:  # 다른 값이 있으면
                        all_same = False
                        break
                if not all_same:
                    break
            
            # 모든 값이 같으면 리프 노드로 처리
            if all_same:
                return Node(val == 1, True)  # (값, isLeaf=True)
            
            # 그리드를 4등분하여 재귀적으로 처리
            n = n // 2  # 그리드 크기를 절반으로
            # 각 사분면에 대해 재귀 호출
            topLeft = helper(n, row, col)  # 좌상단
            topRight = helper(n, row, col + n)  # 우상단
            bottomLeft = helper(n, row + n, col)  # 좌하단
            bottomRight = helper(n, row + n, col + n)  # 우하단
            
            # 4개의 자식 노드를 가진 내부 노드 반환
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        n = len(grid)  # 그리드의 크기
        return helper(n, 0, 0)  # 전체 그리드에 대해 시작