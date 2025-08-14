#include <ranges>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> char_index;
        int max_length = 0;
        int start = 0;

        for (auto const& [end, ch] : ranges::views::enumerate(s))
        // 여기서는 end가 long이 됨; enumerate가 size_t를 반환(64bit에서 long)
        {
            if (char_index.contains(ch) && char_index[ch] >= start)
            {
                start = char_index[ch] + 1;
            }
            
            char_index[ch] = end;
            max_length = max(max_length, static_cast<int>(end) - start + 1);
        }

        return max_length;
    }
};