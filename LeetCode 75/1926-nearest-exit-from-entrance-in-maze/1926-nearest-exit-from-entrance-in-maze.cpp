class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        const int m = maze.size();
        const int n = maze[0].size();
        const int dx[4] = {0, 0, 1, -1};
        const int dy[4] = {1, -1, 0, 0};

        struct Cell {
            int x, y, steps;
            Cell(int _x, int _y, int _steps) : x(_x), y(_y), steps(_steps) {}
        };

        queue<Cell> q;
        vector<vector<bool>> visited(m, vector<bool>(n, false));

        const int startX = entrance[0];
        const int startY = entrance[1];

        q.push(Cell(startX, startY, 0));
        visited[startX][startY] = true;

        while (!q.empty()) {
            Cell current = q.front();
            q.pop();

            int x = current.x;
            int y = current.y;
            int steps = current.steps;

            if ((x == 0 || x == m - 1 || y == 0 || y == n - 1) && (x != startX || y != startY)) return steps;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                // 유효한 이동인지 확인
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && maze[nx][ny] == '.' && !visited[nx][ny]) {
                    q.push(Cell(nx, ny, steps + 1));
                    visited[nx][ny] = true;
                }
            }
        }

        return -1;
    }
};