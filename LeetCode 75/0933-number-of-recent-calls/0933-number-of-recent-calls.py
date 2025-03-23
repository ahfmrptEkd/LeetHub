from collections import deque

class RecentCounter:

    def __init__(self):
        # deque로 양쪽에서 O(1) 삽입/삭제
        self.requests = deque()

    def ping(self, t: int) -> int:
        # 현재 시간 t에 새 요청 추가
        self.requests.append(t)

        # 시간 범위 [t-3000, t] 를 벗어난 요청 제거
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # 남은 요청 수 반환
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)