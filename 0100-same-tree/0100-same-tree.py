# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 재귀적으로 두 트리가 동일한지 확인하는 함수
        
        # 기저 조건 1: 두 노드가 모두 None인 경우
        # 두 노드가 모두 없으면 구조적으로 동일함
        if not p and not q:
            return True

        # 기저 조건 2: 두 노드 중 하나만 None이거나 두 노드의 값이 다른 경우
        # 1. p가 None이고 q가 None이 아니거나
        # 2. p가 None이 아니고 q가 None이거나
        # 3. 두 노드 모두 있지만 값이 다른 경우
        # 이 경우들은 모두 트리가 다름을 의미
        if not p or not q or p.val != q.val:
            return False
        
        # 재귀 호출: 두 노드의 값이 같은 경우, 왼쪽 서브트리와 오른쪽 서브트리도 각각 같은지 확인
        # 두 서브트리가 모두 같아야만 전체 트리가 같음
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)