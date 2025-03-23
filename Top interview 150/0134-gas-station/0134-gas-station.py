class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 한 바퀴를 돌 수 있는 수 가 있는지 아는게 중요
            # a 에서 b 가는 사이 기름이 떨어진다면 그건 그 사이 값 어디에서 시작해도 도착 불가
            # 한 바퀴를 돈다 그리고 무조건 돌 수 있는 조건이라면 답은 최소한개는 있다.
            # 그 뒤 b에서 부탁 시작하면 된다.

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        
        return start