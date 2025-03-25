# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. 연결 리스트의 중간을 찾는다.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 절반을 뒤집는다.
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # # 3. 최대 합 구하기
        max_twin_sum = 0
        left = head
        right = prev
        
        while right:
            max_twin_sum = max(max_twin_sum, left.val + right.val)
            left = left.next
            right = right.next
        
        return max_twin_sum