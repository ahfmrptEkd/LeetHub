class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Kadane's Algorithm은 배열에서 최대 연속 부분합(maximum subarray sum)을 O(n) 시간에 찾는 동적 프로그래밍 알고리즘
        int maxEnd = nums[0];
        int maxCurr = nums[0];

        for (int i = 1; i < nums.size(); i++)
        {
            int n = nums[i];
            maxEnd = max(n, n + maxEnd);
            maxCurr = max(maxCurr, maxEnd);
        }

        return maxCurr;
    }
};