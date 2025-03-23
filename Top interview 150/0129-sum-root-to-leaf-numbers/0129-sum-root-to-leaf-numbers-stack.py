# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # (노드, 현재까지 만들어진 숫자)를 저장할 스택
        stack = [(root, root.val)]
        total_sum = 0

        while stack:
            node, curr_num = stack.pop()

            # leaf 노드면 지금까지 만든 숫자를 결과에 더함
            if not node.left and not node.right:
                total_sum += curr_num

            # 오른쪽 자식이 있으면 스택에 추가
            if node.left:
                # 현재 숫자에 10을 곱하고 자식의 값을 더함
                stack.append((node.left, curr_num * 10 + node.left.val))
            
            # 오른쪽 자식이 있으면 스택에 추가
            if node.right:
                stack.append((node.right, curr_num * 10 + node.right.val))
        
        return total_sum