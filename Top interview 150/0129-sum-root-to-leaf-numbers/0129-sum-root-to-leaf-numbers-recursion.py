# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def sumNumbers(self, root: Optional[TreeNode]) -> int:
       # 총합을 저장할 인스턴스 변수 선언
       self.total = 0

       def recursion(node, num):
           # 베이스 케이스: 빈 트리인 경우 0 반환
           if not node:
               return 0
           
           # 현재까지의 숫자(num)에 10을 곱하고 현재 노드의 값을 더해서 
           # 새로운 숫자를 만듦 (예: num=1, node.val=2 이면 12가 됨)
           current = num * 10 + node.val

           # 리프 노드인 경우 (자식이 없는 경우)
           # 지금까지 만들어진 숫자를 total에 더하기
           if not node.left and not node.right:
                self.total += current
                return  # 또는 return 0
           
           # 리프 노드가 아닌 경우 왼쪽, 오른쪽 재귀 호출
           recursion(node.left, current)
           recursion(node.right, current)
       
       # 초기 호출: 루트 노드부터 시작하고 초기 숫자는 0
       recursion(root, 0)
       return self.total