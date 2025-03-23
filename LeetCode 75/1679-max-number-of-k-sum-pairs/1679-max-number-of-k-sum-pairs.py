class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        1, r 을 이용한 포인터

        k의 값을 만족하는 nums[l], nums[r]을 찾아 리스트에서 제거후
        총 몇번의 연산이 가능한지 계산하는 프로그램
        
        0.정렬된 array 안에서 서로 양끝단에서 시작해서 찾아가면서 연산
            범위 => left가 right보다 작을 때 까지만.
        1.첫 원소가 k보다 크다면, 그런 연산은 불가능하니까 그냥 다음 인덱스로 패스
        2.더한 연산값이 k에 미달이면 다음 값을 더할때까지 찾기.
            l을 왼쪽으로 한번더 보내 연산
        3.합이 더 초과라면, 반대로
            r을 오른쪽으로 한번더 보내 연산


        N 이 10만을 넘기 때문에, O(N) 알고리즘만으로 풀기.
        """
        nums.sort() # 정렬

        l = 0
        r = len(nums) - 1
        answer = 0

        while l < r:
            if (nums[l] + nums[r]) == k:    # 둘의 연산이 같다면?
                answer += 1
                l += 1
                r -= 1
            elif (nums[l] + nums[r]) < k:   # 둘의 연산이 부족하다면?
                l += 1
            else:
                # 둘의 연산이 초과?
                r -= 1
        
        return answer