# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 트리의 각 레벨별 평균값을 반환하는 함수
        
        queue = deque([root])  # 루트 노드를 시작으로 하는 큐 초기화
        res = []  # 각 레벨의 평균값을 저장할 결과 리스트
        
        while queue:  # 큐가 빌 때까지 반복
            size = len(queue)  # 현재 레벨의 노드 개수
            total = 0  # 현재 레벨의 값들의 합
            
            for i in range(size):  # 현재 레벨의 모든 노드를 처리
                node = queue.popleft()  # 큐에서 노드를 하나 꺼냄
                total += node.val  # 현재 노드의 값을 합계에 추가
                
                # 왼쪽 자식이 있으면 큐에 추가
                if node.left:
                    queue.append(node.left)
                # 오른쪽 자식이 있으면 큐에 추가
                if node.right:
                    queue.append(node.right)
            
            res.append(total/size)  # 현재 레벨의 평균값을 결과 리스트에 추가
        return res  # 모든 레벨의 평균값 리스트 반환