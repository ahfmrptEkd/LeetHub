class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b){
            return a[0] < b[0];
        });

        vector<vector<int>> merged;

        for (const auto& item : intervals) {
            // 조건1: merged가 비어있거나(첫 구간인 경우)
            // 조건2: 현재 구간의 시작점이 이전 구간의 끝점보다 큰 경우(겹치지 않는 경우)
            if (merged.empty() || merged.back()[1] < item[0]) {
                // 새로운 구간으로 추가
                merged.push_back(item);
            } else {
                // 구간이 겹치는 경우, 이전 구간의 끝점을 더 큰 값으로 업데이트
                // 예: [1,3], [2,6] -> [1,6]
                merged.back()[1] = max(merged.back()[1], item[1]);
            }
        }

        // 병합이 완료된 구간들 반환
        return merged;

    }
};