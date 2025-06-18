class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();

        // 쌍으로 묶기
        vector<pair<int, int>> pairs;
        for (int i = 0; i < n ; i++) {
            pairs.push_back({nums1[i], nums2[i]});
        }

        sort(pairs.begin(), pairs.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
                    return a.second > b.second; // nums2 값 기준 내림차순
            });
        
        priority_queue<int, vector<int>, greater<int>> minHeap;
        long long sumOfNums1 = 0;
        long long maxScore = 0;

        for (const auto& p : pairs) {
            int n1 = p.first;
            int n2 = p.second;

            // 현재 nums1 값을 heap 에 추가
            minHeap.push(n1);
            sumOfNums1 += n1;

            // 힙 크기 초과시 가장 작은 값 제거
            if (minHeap.size() > k) {
                sumOfNums1 -= minHeap.top();
                minHeap.pop();
            }

            // 힙크기 k에 도착시 스코어 갱신
            if (minHeap.size() == k) {
                long long score = sumOfNums1 * n2;
                maxScore = max(maxScore, score);
            }
        }

        return maxScore;

    }
};