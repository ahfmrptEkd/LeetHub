class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 빈 리스트나 노드가 1개인 경우
        if not head or not head.next:
            return False
            
        # 두 포인터 사용: 거북이(slow)와 토끼(fast)
        slow = head
        fast = head
        
        # fast가 끝에 도달할 때까지 이동
        while fast and fast.next:
            slow = slow.next       # 한 칸 이동
            fast = fast.next.next  # 두 칸 이동
            
            # 두 포인터가 만나면 cycle이 있다는 의미
            if slow == fast:
                return True
                
        return False