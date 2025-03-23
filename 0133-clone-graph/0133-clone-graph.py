"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # 노드의 정보를 저장
        copies = {}

        def dfs(node):
            # 저장 된 노드인경우 노드의 정보를 반환
            if node in copies:
                return copies[node]
            
            # 아닌 경우, 노드를 새로이 Node 로 copies에 저장
            copy = Node(node.val)
            copies[node] = copy

            # 노드의 이웃에 대한 정보를 가져오며 & 새로이 저장.
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy     
        
        return dfs(node)