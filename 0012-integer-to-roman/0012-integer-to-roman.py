class Solution:
    def prepare_num(self, num) -> list:
        num_str = str(num)
        length = len(num_str)
        container = []
        for i, digit in enumerate(num_str):
            place_value = 10 ** (length - i - 1)
            container.append(int(digit)*place_value)
        return container

    def intToRoman(self, num: int) -> str:
        math = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

        ans = []
        for value in self.prepare_num(num):
            for roman_value, roman_symbol in math.items():
                while value >= roman_value:
                    ans.append(roman_symbol)
                    value -= roman_value
        
        return ''.join(ans)
