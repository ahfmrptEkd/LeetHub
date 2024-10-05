class Solution:
    def intToRoman(self, num: int) -> str:
        # 받은 숫자를 줄여 나가는 식으로 딕셔너리를 순환하게 한다.
        math = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        sorted_math = sorted(math.items(), key=lambda x:x[1], reverse=True)     # 역순으로 정렬하여 큰값 부터 줄여나가게끔
        
        ans = ""
        for symbol, value in sorted_math:
            while num >= value:     # 숫자가 현재 값보다 작아지면 다음 값과 비교
                ans += symbol
                num -= value
        
        return ans