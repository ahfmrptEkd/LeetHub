# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
       # 최소 차이값과 이전 노드의 값을 저장할 변수 초기화
       self.min_diff = float('inf')  # 최소 차이를 무한대로 초기화
       self.prev = None              # 이전 노드의 값은 None으로 초기화

       def inorder(node):
           # 노드가 없으면 종료
           if not node:
               return 
           
           # 왼쪽 서브트리 순회 (BST에서 현재 노드보다 작은 값들)
           inorder(node.left)

           # 현재 노드 처리
           # 이전 값이 있으면 차이를 계산하여 최소값 갱신
           if self.prev is not None:
               self.min_diff = min(self.min_diff, abs(node.val - self.prev))
           self.prev = node.val  # 현재 값을 이전 값으로 저장

           # 오른쪽 서브트리 순회 (BST에서 현재 노드보다 큰 값들)
           inorder(node.right)

       # 중위순회 시작
       inorder(root)
       return self.min_diff