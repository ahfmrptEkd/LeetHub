# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """복제된 노드들은 모조리 삭제.
        복제의 시작 인덱스
        끝 인덱스
        그 전 노드를 가지고 다음 노드와 연결해줘야 함.
        """
        # 빈 연결 리스트인 경우 처리
        if not head:
            return None

        # 더미 노드 생성 (첫 노드 삭제 처리를 쉽게 하기 위함)
        dummy = ListNode(0)
        dummy.next = head

        # prev: 마지막으로 확인된 중복되지 않은 노드를 가리킴
        prev = dummy
        # curr: 현재 검사 중인 노드
        curr = head
        
        # 현재 노드와 다음 노드가 존재하는 동안 반복
        while curr and curr.next:
            # 현재 노드가 다음 노드와 값이 같은 경우 (중복 발견)
            if curr.val == curr.next.val:
                # 중복되는 값이 끝날 때까지 curr 포인터 이동
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # 마지막 중복 값을 지나 다음 노드로 이동
                curr = curr.next
                # prev의 next를 중복이 끝난 지점으로 연결 (중복 값들 건너뛰기)
                prev.next = curr
            # 중복이 아닌 경우
            else:
                # prev를 현재 노드로 이동 (중복되지 않은 노드 저장)
                prev = curr
                # curr을 다음 노드로 이동
                curr = curr.next

        # 더미 노드의 next를 반환 (실제 연결 리스트의 시작점)
        return dummy.next