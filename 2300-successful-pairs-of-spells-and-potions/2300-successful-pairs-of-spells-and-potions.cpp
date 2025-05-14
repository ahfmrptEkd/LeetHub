class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<int> result(spells.size());
        sort(potions.begin(), potions.end());
        int m = potions.size();

        for (int i = 0; i < spells.size(); i++) {
            int left = 0;
            int right = m - 1;
            long long spell = spells[i];
            
            // 최적화: 가장 강한 물약도 조건을 만족하지 않으면 0 반환
            if ((long long)spell * potions[right] < success) {
                result[i] = 0;
                continue;
            }
            
            // 이진 탐색
            while (left < right) {
                int mid = left + (right - left) / 2;
                
                if ((long long)spell * potions[mid] >= success) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            
            // 최종 위치가 조건을 만족하는지 확인
            if ((long long)spell * potions[left] >= success) {
                result[i] = m - left;
            } else {
                result[i] = 0;
            }
        }
        
        return result;
    }
};