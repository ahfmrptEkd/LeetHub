# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
   def maxDepth(self, root: Optional[TreeNode]) -> int:
       # 빈 트리인 경우 0 반환
       if not root:
           return 0
       
       # (깊이, 노드) 쌍을 저장하는 큐 초기화
       queue = deque([(1, root)])
       max_depth = 0

       while queue:
           # 현재 깊이와 노드 추출
           depth, node = queue.popleft()
           # 최대 깊이 갱신
           max_depth = max(depth, max_depth)

           # 왼쪽 자식이 있으면 큐에 추가
           if node.left is not None:
               queue.append((depth + 1, node.left))
           # 오른쪽 자식이 있으면 큐에 추가 
           if node.right is not None:
               queue.append((depth + 1, node.right))
       return max_depth