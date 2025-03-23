# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        Morris Traversal을 사용한 이진 트리 평탄화
        시간복잡도: O(N) - 각 노드를 최대 2번 방문
        공간복잡도: O(1) - 추가 공간 사용하지 않음
        """
        # 현재 처리 중인 노드
        current = root
        
        while current:
            if current.left:
                # left 서브트리가 있는 경우
                # left 서브트리의 가장 오른쪽 노드를 찾음
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # 현재 노드의 right 서브트리를 
                # left 서브트리의 가장 오른쪽에 연결
                predecessor.right = current.right
                # left 서브트리를 right로 이동
                current.right = current.left
                # left를 None으로 설정
                current.left = None
            
            # 다음 노드로 이동
            current = current.right