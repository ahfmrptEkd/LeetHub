class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // calculate freqency
        unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;

        // bucket => idx = freqency, value = number
        int n = nums.size();
        vector<vector<int>> buckets(n + 1);
        for (const auto &p : freq)
        {
            int number = p.first;
            int count = p.second;
            buckets[count].push_back(number);
        }

        // collect a high frequency numbers for k amount.
        vector<int> result;
        for (int f = n; f >= 1 && result.size() < k; f--)
        {
            for (int val : buckets[f])
            {
                result.push_back(val);
                if (result.size() == k) break;
            }
        }

        return result;
    }
};