# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       self.count = 0  # 현재까지 방문한 노드의 수를 추적
       self.result = 0  # k번째로 작은 값을 저장할 변수

       def inorder(node):
           # 기저 조건: 노드가 없으면 종료
           if not node:
               return
           
           # 1. 왼쪽 서브트리 탐색 (현재 노드보다 작은 값들)
           inorder(node.left)

           # 2. 현재 노드 처리
           self.count += 1           # 방문한 노드 수 증가
           if self.count == k:       # k번째 노드를 찾으면
               self.result = node.val # 해당 값을 저장하고
               return                # 탐색 종료
           
           # 3. 오른쪽 서브트리 탐색 (현재 노드보다 큰 값들)
           inorder(node.right)

       # 중위 순회 시작 (BST에서는 오름차순 순회)
       inorder(root)
       return self.result
