class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 코스 수강 가능 여부를 확인하는 함수
        # numCourses: 총 코스 수
        # prerequisites: [수강할 과목, 선수과목] 형태의 리스트
        
        # 그래프를 저장할 딕셔너리 초기화
        graph = {}

        # prerequisites를 그래프 형태로 변환
        # x: 수강할 과목, y: 선수과목
        for x, y in prerequisites:
            if x not in graph:
                graph[x] = []
            graph[x].append(y)

        # 이미 확인이 완료된 과목들을 저장하는 집합
        visited = set()
        # 현재 탐색 중인 경로의 과목들을 저장하는 집합 (순환 검사용)
        path = set()
        
        def dfs(course):
            # 현재 과목이 현재 탐색 경로에 있다면 순환이 존재한다는 의미
            # 순환이 있으면 수강이 불가능하므로 False 반환
            if course in path:
                return False
            
            # 이미 방문한 과목이면 수강 가능하다는 의미
            # 이전에 확인이 완료된 과목이므로 True 반환
            if course in visited:
                return True
            
            # 현재 과목을 현재 탐색 경로에 추가
            path.add(course)

            # 현재 과목의 선수과목들을 재귀적으로 확인
            # graph.get(course, []): course가 키로 없으면 빈 리스트 반환
            for next_course in graph.get(course, []):
                # 선수과목 중 하나라도 수강이 불가능하면 False 반환
                if not dfs(next_course):
                    return False

            # 현재 과목의 확인이 끝났으므로 path에서 제거
            path.remove(course)
            # 현재 과목을 방문 완료 집합에 추가
            visited.add(course)
            # 현재 과목은 수강 가능하므로 True 반환
            return True
        
        # 모든 과목에 대해 수강 가능 여부 확인
        for course in range(numCourses):
            # 하나라도 수강이 불가능한 과목이 있다면 False 반환
            if not dfs(course):
                return False

        # 모든 과목이 수강 가능하므로 True 반환
        return True