#include <ranges>

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> s;
        vector<int> answer(temperatures.size(), 0);

        for (auto const& [i, t] : ranges::views::enumerate(temperatures)) {
            while (!s.empty() && temperatures[s.top()] < t) {
                int prevIdx = s.top();
                s.pop();

                answer[prevIdx] = i - prevIdx;
            }

            s.push(i);
        }

        return answer;
    }
};