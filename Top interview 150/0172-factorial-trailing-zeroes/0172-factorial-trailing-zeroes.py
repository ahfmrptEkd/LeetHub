class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 5의 개수를 저장할 변수
        count = 0
        
        # n이 0보다 클 때까지 반복
        while n > 0:
            # n을 5로 나누면서 5의 인수를 찾음
            # 예: n=25일 때
            # 1차: n = 25//5 = 5  (5의 배수 개수: 5개)
            # 2차: n = 5//5 = 1   (25가 추가로 제공하는 5: 1개)
            # 3차: n = 1//5 = 0   (반복 종료)
            n //= 5
            
            # 현재 단계에서 찾은 5의 개수를 더함
            # 예: 25일 때
            # count = 0 + 5 = 5 (첫 단계)
            # count = 5 + 1 = 6 (두 번째 단계)
            count += n
        
        return count