class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # int()의 2번째 parameter는 숫자의 base를 의미 여기서는 2진수
        a = int(a, 2)
        b = int(b, 2)
        res = a+b
        # print(f"a:{a}, b:{b}, sum:{res}, bin(sum):{bin(res)}") # 이해 돕기용 bin()은 2진수로 바꿈 
        return bin(res)[2:] # 0b 는 2진수의 접두사; bin() 접두사를 내보낸다.