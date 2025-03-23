# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       # 노드가 하나뿐일 때는 None 반환
       if not head.next:
           return None

       fast = head
       slow = head

       # fast 포인터를 n만큼 앞으로 이동
       for _ in range(n):
           fast = fast.next
       
       # fast가 None이면 첫 노드를 삭제
       if not fast:
           return head.next
       
       # fast.next가 None일 때까지 이동하면
       # slow는 삭제할 노드 이전 위치에 도달
       while fast.next:
           fast = fast.next
           slow = slow.next
       
       # 삭제할 노드를 건너뛰도록 연결 변경
       slow.next = slow.next.next

       return head