class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        
        def word_transfer(word):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            possible = []

            for i in range(len(word)):
                original = word[i]
                for c in alphabet:
                    if c != original:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordset:
                            possible.append(new_word)
            return possible

        queue = deque([(beginWord, 1)])
        visited = set()
        wordset = set(wordList)

        while queue:
            word, change = queue.popleft()
            if word == endWord:
                return change
            
            words = word_transfer(word)

            for w in words:
                if w not in visited:
                    visited.add(w)
                    queue.append((w, change+1))
        
        return 0
        