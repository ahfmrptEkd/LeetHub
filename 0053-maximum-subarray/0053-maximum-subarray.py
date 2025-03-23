class Solution:
   def maxSubArray(self, nums: List[int]) -> int:
       """Kadane's Algorithm은 배열에서 최대 연속 부분합(maximum subarray sum)을 O(n) 시간에 찾는 동적 프로그래밍 알고리즘"""
       # divide and conquer 방식
       
       def max_cross_sum(left, mid, right):
           # mid를 기준으로 왼쪽으로 확장하며 최대 부분합 찾기
           left_sum = curr = 0
           max_left = float('-inf')
           for i in range(mid, left - 1, -1):
               curr += nums[i]
               max_left = max(max_left, curr)
           
           # mid를 기준으로 오른쪽으로 확장하며 최대 부분합 찾기
           right_sum = curr = 0
           max_right = float('-inf')
           for i in range(mid + 1, right + 1):
               curr += nums[i]
               max_right = max(max_right, curr)
           
           # 왼쪽과 오른쪽 최대 부분합을 합친 값 반환
           return max_left + max_right
       
       def divide_conquer(left, right):
           # 기저 조건: 한 원소만 남았을 때
           if left == right:
               return nums[left]
           
           # 배열을 중간 지점으로 분할
           mid = (left + right) // 2
           
           # 세 가지 경우 중 최대값 반환:
           # 1. 왼쪽 부분의 최대 부분합
           # 2. 오른쪽 부분의 최대 부분합
           # 3. 중간을 걸치는 최대 부분합
           return max(
                       divide_conquer(left, mid),
                       divide_conquer(mid + 1, right),
                       max_cross_sum(left, mid, right)
           )
       
       # 전체 배열에 대해 분할 정복 시작
       return divide_conquer(0, len(nums)-1)
