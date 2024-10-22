from collections import defaultdict
from itertools import product

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        # row
        flat = set(item for row in board for item in row)
        print(flat)
        if len(flat) == 1:
            return True
        for i in range(n):
            dict_num = defaultdict(int)
            for num in board[i]:
                if num == ".":
                    continue
                if num not in dict_num:
                    dict_num[num] += 1
                else:
                    dict_num[num] += 1

            if any(value >= 2 for value in dict_num.values()):
                return False
        # col
        for i in range(n):
            dict_num = defaultdict(int)
            for j in range(n):
                num = board[j][i]
                if num == ".":
                    continue
                if num not in dict_num:
                    dict_num[num] += 1
                else:
                    dict_num[num] += 1
            if any(value >= 2 for value in dict_num.values()):
                return False

        
        combinations = []
        combinations.append(list(product(range(0, 3), range(0,3))))
        combinations.append(list(product(range(0, 3), range(3,6))))
        combinations.append(list(product(range(0, 3), range(6,9))))

        combinations.append(list(product(range(3,6), range(0,3))))
        combinations.append(list(product(range(3,6), range(3,6))))
        combinations.append(list(product(range(3,6), range(6,9))))
        
        combinations.append(list(product(range(6,9), range(0,3))))
        combinations.append(list(product(range(6,9), range(3,6))))
        combinations.append(list(product(range(6,9), range(6,9))))

        for i in range(n):
            dict_num = defaultdict(int)
            for x, y in combinations[i]:
                num = board[x][y]
                if num == ".":
                    continue
                if num not in dict_num:
                    dict_num[num] += 1
                else:
                    dict_num[num] += 1
            if any(value >= 2 for value in dict_num.values()):
                return False


        return True