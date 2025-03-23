class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 두 점 사이의 기울기를 계산하는 헬퍼 함수
        def slope(p1, p2):
            # x좌표가 같으면 수직선이므로 무한대 반환
            if p1[0] == p2[0]:
                return float('inf')
            # 기울기 계산: (y2-y1)/(x2-x1)
            return (p2[1] - p1[1]) / (p2[0] - p1[0])
        
        # 점이 2개 이하면 그대로 반환
        if len(points) <= 2:
            return len(points)
        
        # 한 직선 위에 있는 점의 최대 개수
        max_points = 1

        # 각 점을 기준점으로 잡고 반복
        for i in range(len(points)):  # O(n)
            # 기울기를 key로, 해당 기울기를 가진 점의 개수를 value로 하는 딕셔너리
            slopes = {}
            # 다른 모든 점과의 기울기 계산
            for j in range(len(points)):  # O(n)
                if i != j:  # 자기 자신은 제외
                    s = slope(points[i], points[j])
                    # 같은 기울기를 가진 점의 개수 업데이트
                    # get(s, 1): 기울기 s가 없으면 1(기준점) 반환
                    slopes[s] = slopes.get(s, 1) + 1
            
            # 현재 기준점에서 가장 많은 점을 포함하는 직선 찾기
            if slopes:
                max_points = max(max_points, max(slopes.values()))

        return max_points