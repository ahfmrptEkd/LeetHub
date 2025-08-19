# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       container = [] # 모든 값을 저장할 배열
       
       # 모든 연결 리스트를 순회하며 값을 배열에 저장 O(N)
       for l in lists:
           dummy = ListNode(0)
           dummy.next = l
           dummy = dummy.next
           while dummy:
               container.append(dummy.val)
               dummy = dummy.next
       
       container.sort() # Python의 Timsort 사용: O(N log N)
       
       # 정렬된 배열을 연결 리스트로 변환 O(N)
       dummy = ListNode(0)
       curr = dummy
       for i in container:
           curr.next = ListNode(i)
           curr = curr.next
       
       return dummy.next