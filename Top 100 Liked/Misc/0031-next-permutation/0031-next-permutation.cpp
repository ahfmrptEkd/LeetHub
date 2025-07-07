class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // 1단계: 피벗(pivot) 찾기
        // 뒤에서부터 nums[i] < nums[i+1]인 첫 번째 i 찾기
        int i = nums.size() - 2;
        
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        
        // 2단계: 피벗을 찾지 못한 경우 (전체가 내림차순)
        // 가장 큰 순열이므로 가장 작은 순열로 재배열
        if (i == -1) {
            reverse(nums.begin(), nums.end());  // C++의 reverse() 사용
            return;
        }
        
        // 3단계: nums[i]보다 큰 수 중에서 가장 작은 수 찾기
        int j = nums.size() - 1;
        
        while (nums[j] <= nums[i]) {
            j--;
        }
        
        // 4단계: 피벗과 찾은 수를 교환
        swap(nums[i], nums[j]);
        
        // 5단계: 피벗 이후 부분을 뒤집기
        // i+1부터 끝까지를 오름차순으로 정렬 (뒤집기)
        reverse(nums.begin() + i + 1, nums.end());
    }
};