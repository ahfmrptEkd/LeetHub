# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
       # 각 값의 inorder에서의 위치를 O(1)로 찾기 위한 해시맵
       inorder_map = {val: idx for idx, val in enumerate(inorder)}

       def helper(in_start, in_end, post_start, post_end):
           # 유효하지 않은 범위면 None 반환
           if in_start >= in_end or post_start >= post_end:
               return None

           # postorder의 마지막 값이 현재 서브트리의 root (후위순회 특성)
           root_val = postorder[post_end - 1]
           # 해시맵을 사용해 root가 inorder에서 어디 있는지 O(1)로 찾음
           root_idx = inorder_map[root_val]
           # 찾은 값으로 새로운 노드 생성
           root = TreeNode(root_val)

           # inorder에서 root를 기준으로 왼쪽 서브트리의 크기 계산
           left_size = root_idx - in_start

           # 왼쪽 서브트리 재귀 호출
           # inorder: in_start부터 root 전까지
           # postorder: post_start부터 왼쪽 서브트리 크기만큼
           root.left = helper(in_start, root_idx, post_start, post_start + left_size)
           
           # 오른쪽 서브트리 재귀 호출
           # inorder: root 다음부터 끝까지
           # postorder: 왼쪽 서브트리 다음부터 현재 root 전까지
           root.right = helper(root_idx+1, in_end, post_start + left_size, post_end - 1)
           
           return root

       # 초기 호출: 전체 배열 범위로 시작
       return helper(0, len(inorder), 0, len(postorder))
