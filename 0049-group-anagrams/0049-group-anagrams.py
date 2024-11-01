class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 들어있는 원소가 같다면 같은 아나그램 인덱스로 처리
        # 이차원 배열로 답을 넣는다.
        # {0:{b:1,a:1,t:1}} 이런식으로 찾고 해당하면
        # 0이면 [[0],[],[]]에 append 하면 될 듯 함
        # n^2 임?
        # 정렬을 하면 abcd 처럼?

        dict_word = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in dict_word:
                dict_word[sorted_word].append(word)
            else:
                dict_word[sorted_word] = [word]
        result = [value for value in dict_word.values()]
        return result
