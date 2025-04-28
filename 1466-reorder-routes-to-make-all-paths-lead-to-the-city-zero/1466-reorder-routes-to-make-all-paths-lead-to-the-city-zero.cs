public class Solution {
    public int MinReorder(int n, int[][] connections) {
        // 무방향 그래프 구축
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++){
            graph[i] = new List<int>();
        }

        // 원래 도로 방향 저장
        var originalEdges = new HashSet<(int, int)>();

        foreach (var conn in connections) {
            int from = conn[0], to = conn[1];
            graph[from].Add(to);
            graph[to].Add(from);
            originalEdges.Add((from, to)); // 원래 방향 기억
        }

        bool[] visited = new bool[n];
        int changes = 0;

        DFS(0, graph, originalEdges, visited, ref changes);

        return changes;
    }

    private void DFS(int city, List<int>[] graph, HashSet<(int, int)> originalEdges,
                        bool[] visited, ref int changes) {
        visited[city] = true;

        foreach ( int neighbor in graph[city]) {
            if (!visited[neighbor]) {
                // 원래 방향이 현재 도시 -> 이웃이면 방향을 바꿔야 됨
                if (originalEdges.Contains((city, neighbor))) {
                    changes++;
                }
                DFS(neighbor, graph, originalEdges, visited, ref changes);
            }
        }
    }
}