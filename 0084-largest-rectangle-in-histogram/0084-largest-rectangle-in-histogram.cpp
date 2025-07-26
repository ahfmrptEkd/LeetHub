#include <ranges>

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int area = 0;
        stack<int> s;
        
        for (auto const& [i, h] : ranges::views::enumerate(heights))
        {
            while(!s.empty() && heights[s.top()] > h)
            {
                int height = heights[s.top()];
                s.pop();
                int width = s.empty()? i : i - s.top() - 1;
                area = max(area, height * width);
            }
            s.push(i);
        }

        while(!s.empty()) {
            int height = heights[s.top()];
            s.pop();
            int width = s.empty() ? heights.size() : heights.size() - s.top() - 1;
            area = max(area, height * width);
        }

        return area;
    }
};