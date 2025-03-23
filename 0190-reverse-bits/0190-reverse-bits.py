class Solution:
    def reverseBits(self, n: int) -> int:
        # 결과를 저장할 변수
        result = 0

        # 32비트를 순회
        for i in range(32):
            # 현재 비트 추출
            bit = (n >> i) & 1  # ">>" 오른쪽으로 비트 시프트 "<<" 왼쪽으로 비트 시프트

            # 반대 위치에 비트 설정
            result |= (bit << (31-i))
        
        # "&" == and
        # "|" == or

        return result