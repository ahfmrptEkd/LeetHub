# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 현재 노드(1) + 왼쪽 서브트리의 노드 수 + 오른쪽 서브트리의 노드 수를 반환
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)      