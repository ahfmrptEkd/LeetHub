# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = head

        while fast and fast.next:
            temp = fast.next
            fast.next = temp.next
            temp.next = slow.next
            slow.next = temp
            
            slow = fast
            fast = fast.next
        
        return dummy.next