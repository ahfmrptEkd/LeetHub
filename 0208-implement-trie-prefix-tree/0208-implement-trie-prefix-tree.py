class Trie:
   def __init__(self):
       self.node = {}      # 자식 노드들을 저장할 딕셔너리
       self.is_end = False # 단어의 끝 표시

   def insert(self, word: str) -> None:
       curr = self         # 루트부터 시작
       for c in word:      # 각 문자 순회
           if c not in curr.node:  # 문자가 없으면 새 트라이 생성
               curr.node[c] = Trie()
           curr = curr.node[c]     # 다음 노드로 이동
       curr.is_end = True  # 단어 끝 표시

   def search(self, word: str) -> bool:
       curr = self
       for c in word:      # 각 문자 존재 확인
           if c not in curr.node:
               return False
           curr = curr.node[c]
       return curr.is_end  # 정확한 단어면 True

   def startsWith(self, prefix: str) -> bool:
       curr = self
       for c in prefix:    # prefix의 모든 문자 존재 확인
           if c not in curr.node:
               return False
           curr = curr.node[c]
       return True         # 경로만 존재하면 True