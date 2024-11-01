class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 들어있는 원소가 같다면 같은 아나그램 인덱스로 처리
        # 이차원 배열로 답을 넣는다.
        # {0:{b:1,a:1,t:1}} 이런식으로 찾고 해당하면
        # 0이면 [[0],[],[]]에 append 하면 될 듯 함
        # 정렬을 하면 abcd 처럼?

        # 아나그램 그룹을 저장할 딕셔너리 초기화
        dict_word = {}

        for word in strs:
            # 현재 단어의 문자들을 정렬하여 키로 사용
            # 예: 'eat' -> 'aet', 'tea' -> 'aet'
            sorted_word = ''.join(sorted(word))

            # 정렬된 문자열이 이미 딕셔너리에 있는 경우, 해당 키의 리스트에 현재 단어를 추가
            if sorted_word in dict_word:
                dict_word[sorted_word].append(word)
            else:
                # 새로운 키를 만들고 현재 단어를 포함하는 리스트를 값으로 저장
                dict_word[sorted_word] = [word]

        result = [value for value in dict_word.values()]
        return result