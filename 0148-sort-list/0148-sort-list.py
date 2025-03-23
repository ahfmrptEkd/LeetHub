# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 베이스 케이스: 빈 리스트거나 노드가 1개면 그대로 반환
        if not head or not head.next:
            return head
        
        # 중간점 찾기 (Floyd's Tortoise and Hare)
        slow = head  # 한 칸씩 이동
        fast = head  # 두 칸씩 이동
        prev = None  # slow 이전 노드를 저장하여 리스트를 나눌 때 사용
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        # 리스트를 두 부분으로 나누기
        prev.next = None  # 첫 번째 절반의 끝을 None으로 설정

        # 재귀적으로 각 절반을 정렬
        left = self.sortList(head)    # 첫 번째 절반 정렬
        right = self.sortList(slow)   # 두 번째 절반 정렬

        # 병합을 위한 dummy 노드 생성
        dummy = ListNode(0)
        curr = dummy

        # 두 정렬된 리스트 병합
        while left and right:
            if left.val <= right.val:  # 왼쪽 값이 작거나 같으면
                curr.next = left
                left = left.next
            else:                      # 오른쪽 값이 작으면
                curr.next = right
                right = right.next
            curr = curr.next
        
        # 남은 노드들 연결
        curr.next = left if left else right

        return dummy.next