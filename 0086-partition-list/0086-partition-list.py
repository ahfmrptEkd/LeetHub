# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0)
        over = ListNode(0)
        less_c = less
        over_c = over

        curr = head
        while curr:
            next_node = curr.next
            obj = curr.val

            if obj < x:
                less_c.next = curr
                less_c = curr
            else:
                over_c.next = curr
                over_c = curr
            
            curr.next = None
            curr = next_node
        
        less_c.next = over.next
        less = less.next
        ans = less

        return ans