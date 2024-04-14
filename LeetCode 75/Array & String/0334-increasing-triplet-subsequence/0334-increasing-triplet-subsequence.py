class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        i 는 정해지고 j 와 k는 최소 큼.

        1. 하나씩 지나가며 조건에 부합하는지 체크
        2. 하나라도 그렇다면 true; 다 아닌 경우에는 false
        """
        first = float('inf')
        second = float('inf')

        # 순회하며 숫자를 저장. 조건을 지나가면서 숫자를 업데이트
        # first와 second보다 큰수가 나오면 true를 반환한다.
        ## 해설 first가 second 다음으로 다시 업데이트 되더라도.. 마지막까지 넘어가 조건을 다 통과한 세번째 큰 수가 되기에 인덱스도 조건에 부합함.
        ### 추가로 다시 업데이트 된 first는 인덱스가 비록 second보다 클 지라도 그전 작은수가 인덱스로 있으며; 그 인덱스는 second의 인덱스보다 작기에 통과함.
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False