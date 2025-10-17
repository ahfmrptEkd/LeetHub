public class Solution {
    public string LongestPalindrome(string s) {
        int n = s.Length;
        if (n == 0) {
            return "";
        }
        
        // dp[i,j] = s[i...j]가 팰린드롬인지 여부
        bool[,] dp = new bool[n, n];
        
        int maxLength = 1;
        int start = 0;
        
        // 모든 한 글자는 팰린드롬
        for (int i = 0; i < n; i++) {
            dp[i, i] = true;
        }
        
        // 두 글자 팰린드롬 확인
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i, i + 1] = true;
                start = i;
                maxLength = 2;
            }
        }
        
        // 세 글자 이상의 팰린드롬 확인
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;  // 끝 인덱스
                
                // s[i+1...j-1]이 팰린드롬이고 s[i]와 s[j]가 같으면 s[i...j]도 팰린드롬
                if (s[i] == s[j] && dp[i + 1, j - 1]) {
                    dp[i, j] = true;
                    if (length > maxLength) {
                        start = i;
                        maxLength = length;
                    }
                }
            }
        }
        
        return s.Substring(start, maxLength);
    }
}