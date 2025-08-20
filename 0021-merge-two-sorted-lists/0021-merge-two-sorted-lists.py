# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       # 빈 리스트 처리: 둘 다 비었거나, 하나만 있는 경우
       if not list1 and not list2:
           return None
       if not list1:
           return list2
       elif not list2:
           return list1
       
        # dummy 노드 생성
       dummy = ListNode(-1)
       current = dummy
        
       # 두 리스트 모두 값이 있는 동안 비교하며 병합
       while list1 and list2:
           if list1.val <= list2.val:
               current.next = list1
               list1 = list1.next
           else:
               current.next = list2
               list2 = list2.next
           current = current.next
       
       # 남은 노드 처리
       current.next = list1 or list2
       
       return dummy.next