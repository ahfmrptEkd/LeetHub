class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 1); // 첫시작은 무브먼트가 최소 다 1 
        
        for (int i = 1; i < m; i++) {
            cout << i << endl;
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j-1];
            }
        }
        
        return dp[n-1];
    }
};