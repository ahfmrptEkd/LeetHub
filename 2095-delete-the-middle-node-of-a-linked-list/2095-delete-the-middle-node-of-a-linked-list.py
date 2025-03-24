# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 빈 리스트 또는 단일 노드인 경우 처리
        if not head or not head.next:
            return None
        
        # 더미 노드
        dummy = ListNode(0)
        dummy.next = head

        # 2개의 포인터로 위치 설정
        slow = dummy
        fast = head

        # 빠른 포인터가 끝에 도달할 때 까지 이동
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 중간 원소 삭제
        slow.next = slow.next.next

        return dummy.next