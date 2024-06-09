class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # hash map을 dictionary 자료형으로 구현함.
        dic = {}

        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        # 2개의 길이를 비교해서 푼다.
        if len(set(dic.values())) != len(set(arr)):
            return False
        return True