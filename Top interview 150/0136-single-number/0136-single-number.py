class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #XOR 연산 이용 '^'
        """
        XOR(exclusive OR)은 두 비트가 서로 다를 때만 1을 반환
        a ^ a = 0 (같은 숫자를 XOR하면 0이 됨)
        a ^ 0 = a (0과 XOR하면 원래 숫자가 나옴)
        XOR은 교환법칙이 성립함 (a ^ b = b ^ a)
        """

        result = 0
        for n in nums:
            result ^= n
        
        return result