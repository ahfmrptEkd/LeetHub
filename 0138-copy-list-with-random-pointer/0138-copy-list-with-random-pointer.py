"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 빈 리스트인 경우 None 반환
        if not head:
            return None
        
        # 원본 노드를 key로, 복사된 노드를 value로 하는 해시맵 생성
        old_to_copy = {}

        # 첫번째 순회: 모든 노드를 복사하여 해시맵에 저장
        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)  # 현재 노드의 값만 복사
            curr = curr.next
        
        # 두번째 순회: next와 random 포인터를 연결
        curr = head
        while curr:
            # 해시맵을 이용해 복사된 노드들의 next와 random 포인터를 설정
            old_to_copy[curr].next = old_to_copy.get(curr.next)     # next 포인터 연결
            old_to_copy[curr].random = old_to_copy.get(curr.random) # random 포인터 연결
            curr = curr.next
        
        # 복사된 연결 리스트의 head 반환
        return old_to_copy[head]
        