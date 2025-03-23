class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = bin(n)[2:]
        res = 0

        for i in bit:
            if i == "1":
                res += 1
        
        return res