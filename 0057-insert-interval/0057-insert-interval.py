class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 새로운 구간(newInterval)을 기존 구간 리스트(intervals)의 끝에 추가
        intervals.append(newInterval)
        
        # 모든 구간을 시작점(x[0])을 기준으로 오름차순 정렬
        intervals.sort(key= lambda x: x[0])
        
        # 병합된 구간들을 저장할 빈 리스트 생성
        merge = []

        for item in intervals:
            # 조건1: merge가 비어있거나(첫 구간인 경우)
            # 조건2: 현재 구간의 시작점이 이전 구간의 끝점보다 큰 경우(겹치지 않는 경우)
            if not merge or (merge[-1][1] < item[0]):
                # 새로운 구간으로 추가
                merge.append(item)
            else:
                # 구간이 겹치는 경우, 이전 구간의 끝점을 더 큰 값으로 업데이트
                # 예: [1,3], [2,6] -> [1,6]
                merge[-1][1] = max(merge[-1][1], item[1])
        
        # 병합이 완료된 구간들 반환
        return merge