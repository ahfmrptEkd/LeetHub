"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """depth와 node를 넣고 depth가 같으면 옆으로 이어주고 아니면 null로 """
        if not root:
            return None
        
        queue = deque([(1, root)])

        while queue:
            depth, node = queue.popleft()   # 1, root
            size = len(queue) 
            
            # 다음 depth의 노드들을 채우는 곳
            if node.left:
                queue.append((depth+1, node.left))
            if node.right:
                queue.append((depth+1, node.right))
            
            # 여기서 반복문으로 넣어줘야 할 거 같은데 반복문?
            for i in range(size):
                depth, node_next = queue.popleft()
                node.next = node_next

                # 다음 depth의 노드들을 채우는 곳
                if node_next.left:
                    queue.append((depth+1, node_next.left))
                if node_next.right:
                    queue.append((depth+1, node_next.right))
            
                node = node_next

        return root