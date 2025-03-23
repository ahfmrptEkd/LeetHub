# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # (노드, 현재까지의 경로 합) 을 저장할 스택
        stack = [(root, root.val)]
        
        # 스택이 빌 때까지 반복
        while stack:
            # 현재 노드와 경로 합을 스택에서 꺼냄
            node, curr_sum = stack.pop()
            
            # leaf 노드이고 경로 합이 targetSum과 같으면 True 반환
            if not node.left and not node.right and curr_sum == targetSum:
                return True
            
            # 오른쪽 자식이 있으면 스택에 추가
            # (DFS에서 왼쪽을 나중에 처리하기 위해 오른쪽을 먼저 스택에 추가)
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
            
            # 왼쪽 자식이 있으면 스택에 추가
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))
        
        # 모든 경로를 탐색했는데도 못 찾았으면 False 반환
        return False