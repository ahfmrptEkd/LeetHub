# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 1. 순회를 준비
        # 2. node x가 root.val보다 같거나 커야함.
        # 3. 현재 위치의 node x가 root 보다 크다면 good 을 plus
        # 4. 순회를 어떻게 해도 문제 없지만, dfs로 구현 stack.
        need_node = [(root, root.val)]
        good_nodes = 0

        while need_node:
            node, max_val = need_node.pop()

            if node:
                if node.val >= max_val:
                    good_nodes += 1
                    max_val = node.val
                if node.right:
                    need_node.append((node.right, max_val))
                if node.left:
                    need_node.append((node.left, max_val))
        
        return good_nodes