class WordDictionary:
    def __init__(self):
        self.children = {}  
        self.is_end = False 

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:  # 단어의 각 문자에 대해
            if c not in curr.children:  # 현재 문자에 대한 노드가 없으면
                curr.children[c] = WordDictionary()  # 새 노드 생성
            curr = curr.children[c]  # 다음 노드로 이동
        curr.is_end = True  # 단어의 끝 표시

    # 단어를 검색하는 메서드 (와일드카드 '.' 지원)
    def search(self, word: str) -> bool:
        def dfs(curr, i):
            if i == len(word):  # 단어의 끝에 도달
                return curr.is_end
            
            if word[i] == ".":  # 와일드카드 문자인 경우
                for child in curr.children.values():  # 모든 자식 노드 탐색
                    if dfs(child, i+1):  # 재귀적으로 다음 문자 검색
                        return True
                return False
            
            if word[i] not in curr.children:  # 현재 문자에 대한 노드가 없음
                return False
            
            child = curr.children[word[i]]  # 다음 노드로 이동
            return dfs(child, i+1)  # 재귀적으로 다음 문자 검색
        
        return dfs(self, 0)  # 루트 노드에서 검색 시작

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)