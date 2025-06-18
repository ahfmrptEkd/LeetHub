class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();

        // 더 짧은걸 열로 사용
        if (m < n) {
            swap(m, n);
            swap(text1, text2);
        }

        // 2개의 이전 과 현재 행으로 O(n) 공간 만 차지
        vector<int> prev(n + 1, 0);
        vector<int> curr(n + 1, 0);

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // 문자가 같은 경우: 대각선의 값 (이전 값) 에 1 더하기
                if (text1[i - 1] == text2[j - 1]) {
                    curr[j] = prev[j - 1] + 1;
                }
                // 문자가 다를 경우: 위쪽과 왼쪽의 최댓 값     
                else {
                    curr[j] = max(prev[j], curr[j-1]);
                }
            }

            prev = move(curr); // prev = curr 같지만, move은 O(1) 복잡도, '=' 은 O(n)
            curr.assign(n+1, 0);
        }

        return prev[n];
    }
};