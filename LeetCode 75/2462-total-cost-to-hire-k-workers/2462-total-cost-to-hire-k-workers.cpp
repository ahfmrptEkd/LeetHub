class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        int n = costs.size();

        // 힙 : {비용:인덱스} - 비용이 같으면 작은게 우선
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

        int left = 0; 
        int right = n - 1;
        long totalCost = 0;

        // 초기 앞쪽과 뒷쪽의 후보를 큐에 추가
        for (int i = 0; i < candidates && left <= right; i++) {
            pq.push({costs[left], left});
            ++left;
        }

        for (int i = 0; i < candidates && right >= left; i++) {
            pq.push({costs[right], right});
            --right;
        }

        // k 명의 근로자 고용
        for (int i = 0; i < k; i++) {
            if (pq.empty()) break;

            // 가장 비용이 낮은 근로자 선택
            auto [cost, idx] = pq.top();
            pq.pop();
            totalCost += cost;

            // 새로운 후보자 추가 (필요의 경우)
            if (left <= right) {
                if (idx < left) {
                    // 앞쪽에 근로자 선택했음으로 새로운 앞쪽 후보 추가
                    pq.push({costs[left], left});
                    ++left;
                }
                else {
                    // 뒤쪽 근로자 선택 새로운 뒤쪽 후보 추가
                    pq.push({costs[right], right});
                    --right;
                }
            }
        }
        return totalCost;
    }
};