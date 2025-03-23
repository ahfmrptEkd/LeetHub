# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # BFS를 위한 큐 초기화, 시작 노드 추가
        queue = deque([root])
        # 오른쪽에서 보이는 노드들을 저장할 결과 리스트
        res = []

        # 큐가 빌 때까지 반복 (모든 레벨을 순회)
        while queue:
            # 현재 레벨의 노드 개수
            level_size = len(queue)
            
            # 현재 레벨의 모든 노드를 처리
            for i in range(level_size):
                node = queue.popleft()  # 큐에서 노드 추출
                
                # 현재 레벨의 마지막 노드인 경우 (= 오른쪽에서 보이는 노드)
                if i == level_size - 1:
                    res.append(node.val)
                
                # 왼쪽 자식을 큐에 추가
                if node.left:
                    queue.append(node.left)
                # 오른쪽 자식을 큐에 추가
                if node.right:
                    queue.append(node.right)

        return res