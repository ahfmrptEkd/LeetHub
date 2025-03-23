# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 전역으로 최대값을 저장
        # float('-inf')로 초기화하는 이유: 모든 노드가 음수일 수 있기 때문
        self.max_sum = float('-inf')
        
        def dfs(node):
            # 베이스 케이스: 노드가 없는 경우
            if not node:
                return 0
            
            # 왼쪽, 오른쪽 서브트리의 최대 경로 합을 구함
            # max(0, ...)를 사용하는 이유: 음수인 경우 그 경로를 선택하지 않는 것이 더 나음
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            
            # 현재 노드를 포함하는 경로의 최대값을 갱신
            # left + node.val + right: 현재 노드를 중심으로 하는 경로
            self.max_sum = max(self.max_sum, left + node.val + right)
            
            # 상위 노드에서 사용할 수 있는 최대 경로 값을 반환
            # 상위에서는 left와 right 중 하나만 선택할 수 있음
            return max(left, right) + node.val
        
        dfs(root)
        return self.max_sum