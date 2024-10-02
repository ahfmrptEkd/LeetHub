class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 한 바퀴를 돌 수 있는 수 가 있는지 아는게 중요

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