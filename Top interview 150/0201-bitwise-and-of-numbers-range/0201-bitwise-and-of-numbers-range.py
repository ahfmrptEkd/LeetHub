class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # left와 right가 같아질 때까지 오른쪽으로 시프트
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        # 결과를 다시 왼쪽으로 시프트
        return left << shift