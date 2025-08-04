class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        // step 1 - transpose matrix
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++) // avoid same index between i and j
            {
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        // step 2 - revserse each rows
        // 90 degree = transpose -> row reverse
        // 180 =       row reverse -> column reverse
        // 270 =       row reverse -> transpose
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n / 2; j++)
            {
                swap(matrix[i][j], matrix[i][n - 1 - j]);
            }
        }
    }
};