# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node, min_val = float('-inf'), max_val = float('inf')):
            if not node:
                return True

            # 왼쪽 서브트리 체크
            # min_val은 유지, max_val은 현재 노드값으로 제한
            if not inorder(node.left, min_val, node.val):
                return False

            # 현재 노드의 값이 유효 범위 내에 있는지 체크
            # min_val보다 커야 하고(오른쪽 서브트리 조건) 
            # max_val보다 작아야 함(왼쪽 서브트리 조건)
            if node.val <= min_val or node.val >= max_val:
                return False

            # 오른쪽 서브트리 체크
            # min_val은 현재 노드값으로 제한, max_val은 유지
            if not inorder(node.right, node.val, max_val):
                return False
            return True
        
        return inorder(root)