# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 빈 트리인 경우 빈 리스트 반환
        if not root:
            return []
        
        queue = deque([root])  # 루트 노드로 큐 초기화
        res = []  # 레벨 순서대로 노드값을 저장할 결과 리스트
        
        while queue:  # 큐가 빌 때까지 반복
            size = len(queue)  # 현재 레벨의 노드 개수
            container = []  # 현재 레벨의 노드값을 저장할 임시 리스트
            
            for i in range(size):  # 현재 레벨의 모든 노드를 처리
                node = queue.popleft()  # 큐에서 노드를 하나 꺼냄
                container.append(node.val)  # 현재 노드의 값을 임시 리스트에 추가
                
                # 왼쪽, 오른쪽 자식이 있으면 큐에 추가
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(container)  # 현재 레벨의 노드값들을 결과 리스트에 추가
        return res