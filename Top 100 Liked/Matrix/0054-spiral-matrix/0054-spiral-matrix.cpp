class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        set<pair<int, int>> visited;
        vector<int> result;
        int row = 0, col = 0;
        
        vector<pair<int, int>> directions = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        int dir = 0;
        
        auto valid_pos = [&](int row, int col) -> bool {
            return (0 <= row && row < m && 0 <= col && col < n && 
                    visited.find({row, col}) == visited.end());
        };
        
        while (visited.size() < m * n) {
            if (valid_pos(row, col)) {
                visited.insert({row, col});
                result.push_back(matrix[row][col]);
                
                int next_row = row + directions[dir].first;
                int next_col = col + directions[dir].second;
                
                if (valid_pos(next_row, next_col)) {
                    row = next_row;
                    col = next_col;
                } else {
                    dir = (dir + 1) % 4;
                    row += directions[dir].first;
                    col += directions[dir].second;
                }
            }
        }
        
        return result;
    }
};