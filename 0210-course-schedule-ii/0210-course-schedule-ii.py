from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 그래프 초기화 - O(E)
        graph = defaultdict(list)
        for x, y in prerequisites:  # O(E) - 모든 간선을 순회
            graph[x].append(y)      # O(1) - 리스트 append
        
        # 방문 기록용 자료구조 초기화 - O(1)
        visited = set()  # 완전히 처리된 노드 집합
        path = set()     # 현재 DFS 경로상의 노드 집합
        res = []         # 결과 저장용 리스트

        def dfs(course):  # 총 시간복잡도: O(V + E)
            # 사이클 검사 - O(1)
            if course in path:    # set 검색 O(1)
                return False
            if course in visited: # set 검색 O(1)
                return True

            # 현재 경로에 노드 추가 - O(1)
            path.add(course)      # set add O(1)

            # 인접 노드 순회 - 각 노드당 한 번씩만 방문하므로 총 O(E)
            for next_course in graph.get(course, []):  # 최악의 경우 O(E)
                if not dfs(next_course):               # 재귀 호출
                    return False

            # 백트래킹 및 결과 기록 - O(1)
            path.remove(course)     # set remove O(1)
            visited.add(course)     # set add O(1)
            res.append(course)      # list append O(1)
            return True
        
        # 모든 과목에 대해 DFS 수행 - O(V)
        # 각 노드는 한 번만 방문되므로(visited set으로 관리),
        # 전체 DFS의 총 시간복잡도는 O(V + E)
        for course in range(numCourses):  # O(V)
            if not dfs(course):
                return []  # 사이클이 있는 경우
        
        return res