class Solution:
   def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
       from collections import deque
       
       def word_transfer(word):
           # 알파벳 문자열 정의
           alphabet = "abcdefghijklmnopqrstuvwxyz"
           possible = []  # 변환 가능한 단어들을 저장할 리스트

           # 현재 단어의 각 위치에서
           for i in range(len(word)):
               original = word[i]  # 원래 문자 저장
               # 모든 알파벳에 대해
               for c in alphabet:
                   if c != original:  # 현재 문자와 다른 경우에만
                       # 해당 위치의 문자만 변경하여 새로운 단어 생성
                       new_word = word[:i] + c + word[i+1:]
                       # 생성된 단어가 wordset에 있으면 가능한 단어 리스트에 추가
                       if new_word in wordset:
                           possible.append(new_word)
           return possible  # 가능한 모든 변환 단어 반환

       # BFS를 위한 큐 초기화 (시작 단어와 변환 횟수)
       queue = deque([(beginWord, 1)])
       visited = set()  # 방문한 단어들을 저장할 set
       wordset = set(wordList)  # 단어 리스트를 set으로 변환하여 검색 효율성 향상

       # BFS 시작
       while queue:
           word, change = queue.popleft()  # 현재 단어와 변환 횟수
           if word == endWord:  # 목표 단어에 도달하면
               return change    # 현재까지의 변환 횟수 반환
           
           # 현재 단어에서 변환 가능한 모든 단어 받아오기
           words = word_transfer(word)

           # 각 변환 가능한 단어에 대해
           for w in words:
               if w not in visited:  # 방문하지 않은 단어만 처리
                   visited.add(w)    # 방문 표시
                   queue.append((w, change+1))  # 큐에 추가 (변환 횟수 1 증가)
       
       return 0 