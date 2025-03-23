# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
       # 빈 입력 처리
       if not preorder or not inorder:
           return None
       
       # preorder의 첫 번째 값으로 루트 노드 생성
       root = TreeNode(preorder[0])
       # 부모 노드들을 추적하기 위한 스택, 초기값으로 루트 추가
       stack = [root]
       # inorder 배열의 현재 인덱스 (왼쪽 자식들의 처리 여부를 추적)
       in_idx = 0 

       # preorder의 나머지 값들을 순회
       for i in range(1, len(preorder)):
           curr_val = preorder[i]
           # 현재 값으로 새 노드 생성
           curr_node = TreeNode(curr_val)
           # 스택의 top이 현재 노드의 잠재적 부모
           parent = stack[-1]

           # 스택의 top이 inorder의 현재 값과 다르면
           # 아직 왼쪽 자식들을 처리 중
           if stack[-1].val != inorder[in_idx]:
               parent.left = curr_node  # 왼쪽 자식으로 추가
               stack.append(curr_node)  # 스택에 push
           # 스택의 top이 inorder의 현재 값과 같으면
           # 왼쪽 서브트리 처리가 완료되어 오른쪽으로 가야 함
           else:
               # inorder에서 현재 값과 같은 노드를 찾을 때까지
               # 스택에서 노드들을 제거하면서 부모를 찾음
               while stack and stack[-1].val == inorder[in_idx]:
                   parent = stack.pop()
                   in_idx += 1
               parent.right = curr_node  # 오른쪽 자식으로 추가
               stack.append(curr_node)   # 스택에 push
       
       return root  # 완성된 트리의 루트 반환