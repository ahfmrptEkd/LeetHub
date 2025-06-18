class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        // 형태: unordered_map<string, vector<pair<string, double>>> - 변수와 그 변수에 연결된 다른 변수 및 나눗셈 값 저장
        unordered_map<string, vector<pair<string, double>>> graph;
        
        // equations와 values를 순회하며 그래프 구성
        for (int i = 0; i < equations.size(); i++) {
            string x = equations[i][0];
            string y = equations[i][1];
            double val = values[i];
            
            // x/y = val 관계 저장
            graph[x].push_back({y, val});
            // y/x = 1/val 관계도 저장 (역방향 엣지)
            graph[y].push_back({x, 1.0/val});
        }
        
        // 각 쿼리에 대해 결과 계산
        vector<double> results(queries.size());
        for (int i = 0; i < queries.size(); i++) {
            string start = queries[i][0];
            string end = queries[i][1];
            unordered_set<string> visited;
            
            results[i] = dfs(start, end, visited, graph);
        }
        
        return results;
    }
    
private:
    double dfs(const string& start, const string& end, unordered_set<string>& visited, 
               unordered_map<string, vector<pair<string, double>>>& graph) {
        // start 노드가 그래프에 없으면 계산 불가능
        if (graph.find(start) == graph.end()) {
            return -1.0;
        }
        // 시작점이 도착점과 같으면 나누기 결과는 1
        if (start == end) {
            return 1.0;
        }
        
        // 현재 노드 방문 처리
        visited.insert(start);
        
        // 현재 노드와 연결된 모든 노드들 탐색
        for (const auto& pair : graph[start]) {
            string nextNode = pair.first;
            double val = pair.second;
            
            // 방문하지 않은 노드에 대해서만
            if (visited.find(nextNode) == visited.end()) {
                // 다음 노드부터 목표까지의 경로 탐색
                double result = dfs(nextNode, end, visited, graph);
                // 경로를 찾았다면 현재 간선의 값과 곱해서 반환
                if (result != -1.0) {
                    return result * val;
                }
            }
        }
        
        // 모든 경로를 탐색했는데 목표를 못 찾으면 -1.0 반환
        return -1.0;
    }
};