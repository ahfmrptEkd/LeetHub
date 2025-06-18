# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 트리의 리프 노드 시퀀스를 재귀적으로 구하는 헬퍼 함수
        def getLeafSequence(root):
            if not root:  # 기저 조건: 노드가 None인 경우 빈 리스트 반환
                return []
            if not root.left and not root.right:  # 리프 노드인 경우 (자식이 없음)
                return [root.val]  # 리프 노드의 값을 리스트에 담아 반환
            
            # 재귀적으로 왼쪽 서브트리와 오른쪽 서브트리의 리프 노드 시퀀스를 구하고 병합
            # 왼쪽 서브트리의 리프 노드가 먼저 오고, 그 다음 오른쪽 서브트리의 리프 노드가 옴
            return getLeafSequence(root.left) + getLeafSequence(root.right)
        
        # 두 트리의 리프 노드 시퀀스를 비교하여 동일한지 확인
        return getLeafSequence(root1) == getLeafSequence(root2)