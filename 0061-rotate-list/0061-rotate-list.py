# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # 리스트 길이 계산 및 tail 찾기
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        
        # tail을 저장
        tail = curr
        
        # k 최적화
        k = k % length
        if k == 0:
            return head
        
        # tail을 head와 연결하여 원형 리스트 만들기
        tail.next = head
        
        # 새로운 tail 위치 찾기: length - k 만큼 이동
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        
        # 새로운 head 저장 및 리스트 끊기
        new_head = curr.next
        curr.next = None
        
        return new_head