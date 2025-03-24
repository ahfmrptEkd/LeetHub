# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 빈 리스트거나 노드가 하나뿐인 경우 바로 반환
        if not head or not head.next:
            return head
        
        # 더미 노드 생성 (이 문제에서는 실제로 dummy가 필요하진 않지만 사용함)
        dummy = ListNode(0)
        dummy.next = head
        
        # odd: 홀수 인덱스 노드들을 연결할 포인터 (1번째, 3번째, 5번째...)
        odd = head
        
        # even: 짝수 인덱스 노드들을 연결할 포인터 (2번째, 4번째, 6번째...)
        even = head.next
        
        # even_head: 짝수 노드들의 시작점을 저장 (나중에 홀수 리스트 뒤에 연결하기 위함)
        even_head = head.next

        # even과 even.next가 존재할 때까지 반복
        # (even.next가 필요한 이유: odd.next = even.next에서 even.next에 접근해야 함)
        while even and even.next:
            # 홀수 노드의 다음을 짝수 노드 다음의 노드(다음 홀수 노드)로 연결
            odd.next = even.next
            # 홀수 포인터를 방금 연결한 다음 홀수 노드로 이동
            odd = odd.next

            # 짝수 노드의 다음을 홀수 노드 다음의 노드(다음 짝수 노드)로 연결
            even.next = odd.next
            # 짝수 포인터를 방금 연결한 다음 짝수 노드로 이동
            even = even.next
        
        # 홀수 리스트의 마지막을 짝수 리스트의 시작과 연결
        odd.next = even_head

        # 완성된 리스트의 헤드를 반환
        # (dummy.next는 원래의 head와 같음)
        return dummy.next