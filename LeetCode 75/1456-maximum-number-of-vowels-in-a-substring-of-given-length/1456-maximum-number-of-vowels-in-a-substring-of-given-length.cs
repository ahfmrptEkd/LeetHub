public class Solution {
    public int MaxVowels(string s, int k) {
        int res = 0;
        int currnt = 0;
        
        HashSet<char> vowels = new HashSet<char> { 'a', 'e', 'i', 'o', 'u' };

        for (int i = 0; i < s.Length; i++) {
            if (i >= k) {          // 나가는 원소 확인
                if (vowels.Contains(s[i-k])) {
                    currnt -= 1;
                }
            }
            
            if (vowels.Contains(s[i])) {  // i 가 커지기 전까지 윈도우를 확인
                currnt += 1;
            }
            
            res = Math.Max(currnt, res);
        }
        return res;
    }
}