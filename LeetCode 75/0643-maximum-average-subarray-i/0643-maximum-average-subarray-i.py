class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 현재 합 & 큰 합을 k 만큼 초기화
        currsum = maxsum = sum(nums[:k])    # 초기화 할때, 합을 구하면서 첫 윈도우를 하게 됨. 
                                            # 총 3번이 필요한것이 아닌 2번만 필요하게 됨.

        # 끝까지 slide window로 넘어가며 합 변화
        for i in range(k, len(nums)):

            # window가 움직이며 나가는 값은 버리고 들어오는 값 넣기
            currsum += nums[i] - nums[i-k]
            
            # update the max
            maxsum = max(maxsum, currsum)

        return maxsum / k