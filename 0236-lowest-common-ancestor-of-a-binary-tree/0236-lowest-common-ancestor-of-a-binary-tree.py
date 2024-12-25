# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def help(node):
            # 기저 사례: 노드가 None인 경우 None 반환
            if not node:
                return None

            # 현재 노드가 p나 q 중 하나와 일치하면 해당 노드 반환
            # 이는 현재 노드가 LCA가 될 수 있음을 의미
            if node.val == p.val or node.val == q.val:
                return node
            
            # 왼쪽과 오른쪽 서브트리를 재귀적으로 탐색
            left = help(node.left)
            right = help(node.right)

            # 왼쪽과 오른쪽 모두에서 노드를 찾은 경우
            # 현재 노드가 p와 q의 최소 공통 조상임
            if left and right:
                return node
            
            # 한쪽에서만 노드를 찾은 경우, 찾은 쪽의 결과를 반환
            # 이는 p나 q 중 하나를 찾았거나, 이미 LCA를 찾은 경우일 수 있음
            return left if left else right
        
        return help(root)