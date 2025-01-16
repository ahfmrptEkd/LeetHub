class WordDictionary:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        stack = [(self, 0)]  # (노드, 현재 인덱스) 튜플을 저장하는 스택
        
        while stack:
            curr, i = stack.pop()
            
            if i == len(word):  # 단어의 끝에 도달
                if curr.is_end:
                    return True
                continue
                
            if word[i] == ".":  # 와일드카드 문자인 경우
                for child in curr.children.values():
                    stack.append((child, i + 1))
                    
            else:  # 일반 문자인 경우
                if word[i] in curr.children:
                    stack.append((curr.children[word[i]], i + 1))
                    
        return False