# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        링크드 리스트의 left부터 right까지의 부분을 역순으로 만드는 함수
        
        접근 방식:
        1. left 이전까지는 그대로 연결
        2. left부터 right까지는 stack에 저장했다가 역순으로 연결
        3. right 이후는 그대로 연결
        
        시간복잡도: O(n) - 리스트를 한 번 순회
        공간복잡도: O(k) - k는 역순으로 만들 부분의 길이(right-left+1)
        
        Parameters:
            head: 링크드 리스트의 시작 노드
            left: 역순으로 만들 시작 위치 (1-based index)
            right: 역순으로 만들 끝 위치 (1-based index)
            
        Returns:
            역순으로 된 부분을 포함한 전체 링크드 리스트의 head
        """
        if left == right:  # 역순으로 만들 부분이 없으면 그대로 반환
            return head

        curr = head
        dummy = ListNode(0)  # 시작 노드가 변경될 수 있으므로 dummy 노드 사용
        temp = dummy
        idx = 1
        stack = []

        # Phase 1: left 이전까지 그대로 연결
        while curr and idx < left:
            temp.next = curr
            temp = temp.next
            curr = curr.next
            idx += 1
        
        # Phase 2: left부터 right까지 stack에 저장
        while curr and idx <= right:
            stack.append(curr.val)
            curr = curr.next
            idx += 1
        
        # Phase 3: stack에서 꺼내면서 역순으로 연결
        while stack:
            temp.next = ListNode(stack.pop())
            temp = temp.next
        
        # Phase 4: 남은 부분 연결
        temp.next = curr

        return dummy.next
        