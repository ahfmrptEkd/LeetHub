class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        # 32비트 정수의 각 비트 위치를 순회 (0부터 31까지)
        for i in range(32):
            # i번째 비트에서 1의 개수를 카운트
            count = 0
            
            # 배열의 모든 숫자를 확인
            for num in nums:
                # num의 i번째 비트가 1인지 확인
                # 1 << i: 1을 i만큼 왼쪽으로 시프트 (예: i=2면 100(2))
                if num & (1 << i):
                    count += 1
            
            # i번째 비트에서 1의 개수를 3으로 나눈 나머지가 있다면
            # (즉, 한 번만 나타난 숫자의 해당 비트가 1이었다면)
            if count % 3:
                # result의 i번째 비트를 1로 설정
                result |= (1 << i)
        
        # 음수 처리
        # 만약 결과가 음수여야 한다면 (최상위 비트가 1이라면)
        if result >= (1 << 31):
            result -= (1 << 32)  # 2의 보수 처리
        
        return result