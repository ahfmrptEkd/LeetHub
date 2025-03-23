class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 풍선의 위치를 시작점(x[0])을 기준으로 오름차순 정렬
        points.sort(key= lambda x:x[0])
        # 화살로 한번에 터트릴 수 있는 풍선 그룹들을 저장할 리스트
        merge = []

        for p in points:
            # 조건1: merge가 비어있거나(첫 풍선인 경우)
            # 조건2: 현재 풍선의 시작점이 이전 그룹의 끝점보다 큰 경우(겹치지 않는 경우)
            if not merge or (merge[-1][1] < p[0]):
                # 새로운 화살이 필요한 그룹으로 추가
                merge.append(p)
            else:
                # 풍선이 겹치는 경우, 겹치는 구간의 끝점을 더 작은 값으로 업데이트
                # 예: [1,6], [2,4] -> [1,4] (2~4 구간에서만 한 화살로 두 풍선을 터트릴 수 있음)
                merge[-1][1] = min(merge[-1][1], p[1])
        
        # 필요한 최소 화살의 개수(겹치지 않는 그룹의 수) 반환
        return len(merge)