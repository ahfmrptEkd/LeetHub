public class Solution {
    public int FindCircleNum(int[][] isConnected) {
        int n = isConnected.Length;
        bool[] visited = new bool[n];  // 도시 방문 여부를 추적하는 배열
        int provinces = 0;  // 총 province(연결된 구성요소) 수
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {  // 아직 방문하지 않은 도시라면
                provinces++;  // 새로운 province 발견
                DFS(isConnected, visited, i);  // DFS로 연결된 모든 도시 탐색
            }
        }
        
        return provinces;
    }
    
    private void DFS(int[][] isConnected, bool[] visited, int city) {
        visited[city] = true;  // 현재 도시를 방문 처리
        
        // 모든 이웃 도시에 대해
        for (int neighbor = 0; neighbor < isConnected.Length; neighbor++) {
            // 현재 도시와 연결되어 있고 아직 방문하지 않았다면
            if (isConnected[city][neighbor] == 1 && !visited[neighbor]) {
                DFS(isConnected, visited, neighbor);  // 재귀적으로 DFS 수행
            }
        }
    }
}