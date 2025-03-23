# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 리스트가 비어있는 경우 처리
        if not lists:
            return None
            
        # (노드값, 리스트 인덱스, 노드) 형태로 힙에 저장
        heap = []
        
        # 각 리스트의 첫 노드를 힙에 추가
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
        
        dummy = ListNode(0)
        curr = dummy
        
        # 힙이 빌 때까지 반복
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # 다음 노드가 있으면 힙에 추가
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next