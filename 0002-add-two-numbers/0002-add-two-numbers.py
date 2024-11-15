# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       """
       두 개의 역순 링크드 리스트를 받아서 합을 역순 링크드 리스트로 반환
       예: 2->4->3 (342) + 5->6->4 (465) = 7->0->8 (807)
       """
       # 자리올림수(carry) 초기화
       carry = 0
       
       # 결과 링크드 리스트의 시작점 (더미 노드)
       temp = ListNode(0)   
       ans = temp  # 현재 위치를 가리킬 포인터

       # l1이나 l2가 남아있거나 carry가 있으면 계속 진행
       while l1 or l2 or carry:
           # 현재 자리의 두 숫자 가져오기 (없으면 0)
           a = l1.val if l1 else 0
           b = l2.val if l2 else 0

           # 현재 자리의 합과 자리올림수 계산
           total = a + b + carry
           carry = total // 10  # 다음 자리로 올릴 수 
           
           # 새로운 노드 생성 (현재 자리의 값)
           ans.next = ListNode(total % 10)  # 10으로 나눈 나머지가 현재 자리 값
           ans = ans.next  # 다음 노드로 이동

           # 입력 리스트들의 다음 노드로 이동
           l1 = l1.next if l1 else None
           l2 = l2.next if l2 else None
       
       # 더미 노드의 다음 노드부터가 실제 결과
       return temp.next