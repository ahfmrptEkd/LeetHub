# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def has_node(self, curr, k):
        temp = curr

        for _ in range(k):
            if not temp:
                return False
            temp = temp.next
        return True

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        k의 원소를 k-1만큼 그걸 다음것과 연결
        다음 원소가 k 만큼 남았는지 확인 필요
        없으면 나머지는 그대로.
        """
        if k == 1:
            return head

        ans = ListNode(0)
        ans.next = head
        prev = ans
        curr = prev.next
        
        while curr and self.has_node(curr, k):
            for _ in range(k-1):  # k 번 순서 바꾸기
                temp = curr.next    # 다음 노드
                curr.next = temp.next   # 다다음 노드를 봄
                temp.next = prev.next    # 다음 노드가 바뀐 자리의 노드를 보고
                prev.next = temp # 현재 노드가 다음노드가 되는 자리 바뀜.

            ### 여기에 바뀐 마지막 원소의 자리로 봐야하러 같은데.
            prev = curr
            curr = curr.next


        return ans.next