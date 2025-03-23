# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """하나의 이진트리에 대해서 대칭인지 확인하는 함수
        재귀적으로 왼쪽 서브트리와 오른쪽 서브트리를 비교한다.
        
        Args:
            root: 대칭을 확인할 이진 트리의 루트 노드
        
        Returns:
            bool: 트리가 대칭이면 True, 아니면 False
        """
        if not root:
            return True

        def compare(left, right):
            # 양쪽 다 None이면 대칭
            if left is None and right is None:
                return True
            # 한쪽만 None이면 비대칭
            elif left is None or right is None:
                return False
            # 값이 다르면 비대칭
            elif left.val != right.val:
                return False
            
            # 왼쪽의 왼쪽과 오른쪽의 오른쪽을 비교
            # 그리고 왼쪽의 오른쪽과 오른쪽의 왼쪽을 비교
            return compare(left.left, right.right) and compare(left.right, right.left)
        
        return compare(root.left, root.right)