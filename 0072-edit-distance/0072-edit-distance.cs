public class Solution {
    public int MinDistance(string word1, string word2) {
        if (word1.Length < 0) return word2.Length;
        if (word2.Length < 0) return word1.Length;

        if (word1.Length < word2.Length) {
            (word1, word2) = (word2, word1);
        }

        int[] prev = Enumerable.Range(0, word2.Length + 1).ToArray();
        int[] curr = new int[word2.Length + 1];

        for (int i = 1; i <= word1.Length; i++){
            curr[0] = i;
            for (int j = 1; j <= word2.Length; j++){
                if (word1[i-1] == word2[j-1]){
                    curr[j] = prev[j-1];
                }
                else {
                    curr[j] = Math.Min(
                                        curr[j-1] + 1, // 삽입
                                        Math.Min(prev[j] + 1, // 삭제
                                        prev[j-1] + 1) // 대체
                    );
                }
            }

            (prev, curr) = (curr, new int[word2.Length + 1]);
        }

        return prev[word2.Length];
    }
}