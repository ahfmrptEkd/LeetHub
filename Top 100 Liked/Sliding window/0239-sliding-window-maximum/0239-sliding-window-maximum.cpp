class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> container;
        deque<int> dq; // contain indices

        for (int i = 0; i < nums.size(); i++)
        {
            // remove elements over window size;
            // window = [i-k+1, i]
            while(!dq.empty() && dq.front() < i-k+1) dq.pop_front();

            // maintain monotonic order;
            while(!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();

            // add current index;
            dq.push_back(i);

            // if window is filled -> add max val & always front is current max value;
            if (i >= k - 1) container.push_back(nums[dq.front()]);
        }

        return container;
    }
};