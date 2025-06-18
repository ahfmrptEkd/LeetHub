# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        dummy = ListNode(0)
        curr = dummy
        
        while head:
            stack.append(ListNode(head.val))
            head = head.next
        
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        
        return dummy.next
            