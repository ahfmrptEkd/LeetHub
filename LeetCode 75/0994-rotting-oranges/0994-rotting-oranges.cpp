class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;
        
        const int rows = grid.size();
        const int cols = grid[0].size();
        
        // 구조체 대신 pair 사용으로 메모리 효율성 향상
        queue<pair<int, int>> rotten;
        int fresh_count = 0;
        
        // 모든 썩은 오렌지 위치 저장 및 신선한 오렌지 개수 계산
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 2) {
                    rotten.push({r, c});
                } else if (grid[r][c] == 1) {
                    ++fresh_count;
                }
            }
        }
        
        // 이미 신선한 오렌지가 없는 경우
        if (fresh_count == 0) return 0;
        
        // 상수 배열을 사용하여 4방향 이동 표현
        const int dr[] = {-1, 1, 0, 0};
        const int dc[] = {0, 0, -1, 1};
        
        int minutes = 0;
        
        // BFS 수행
        while (!rotten.empty()) {
            // 현재 단계에 있는 모든 썩은 오렌지 처리 (레벨별 BFS)
            int size = rotten.size();
            
            for (int i = 0; i < size; ++i) {
                int r = rotten.front().first;
                int c = rotten.front().second;
                rotten.pop();
                
                // 4방향 탐색
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    
                    // 범위 검사 및 신선한 오렌지인지 확인
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // 오렌지를 썩게 변경
                        --fresh_count;    // 신선한 오렌지 개수 감소
                        rotten.push({nr, nc}); // 새로 썩은 오렌지 큐에 추가
                    }
                }
            }
            
            if (!rotten.empty()) ++minutes;
        }
        
        // 모든 오렌지가 썩었는지 확인
        return (fresh_count == 0) ? minutes : -1;
    }
};