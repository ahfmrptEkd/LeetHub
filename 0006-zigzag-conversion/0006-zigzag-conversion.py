class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):   # 만약 행의 수가 1이거나 문자열의 길이보다 크거나 같으면, 원래 문자열을 그대로 반환합니다.
            return s

        rows = [''] * numRows
        current_row = 0 # 현재 처리 중인 행을 나타냅니다.
        step = 1 #  다음에 이동할 방향을 나타냅니다 (1: 아래로, -1: 위로).

        for char in s:
            rows[current_row] += char

            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
            
            current_row += step
        return ''.join(rows)