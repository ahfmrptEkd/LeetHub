class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # print(ord('a')) # 97
        # print(ord('b')) # 98
        # print(ord('a')-(ord('a')))  # 0
        # print(ord('b')-(ord('a')))  # 1

        # store alphabet frequency
        freq1 = [0] * 26
        freq2 = [0] * 26

        for chr in word1:
            freq1[ord(chr) - ord('a')] += 1
        
        for chr in word2:
            freq2[ord(chr) - ord('a')] += 1

        # compare similiarity of two words; it ensures both contain same set of characters
        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False
        
        freq1.sort()
        freq2.sort()

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        
        return True
        