# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 자체 적인 사이클을 비슷하게 구현. 서로의 다른 경로를 A 와 B로 가게끔 함.  그렇게 해서 같은 
        # 교차하는 경우: 거리 = lenA + lenB - common_part
        if not headA or not headB:
            return None
        
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = headB if pointer_a is None else pointer_a.next
            pointer_b = headA if pointer_b is None else pointer_b.next
        
        return pointer_a