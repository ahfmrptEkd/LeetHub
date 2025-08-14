class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty() || s.empty()) return "";

        // t의 문자들 카운트
        unordered_map<char, int> dict_t;
        for (char c : t)
        {
            dict_t[c]++;
        }
        int required = dict_t.size();

        // s 필터링 t에 포함된 문자들만 추출 w/ index
        vector<pair<int, char>> filtered_s;
        for (int i = 0; i < s.length(); i++)
        {
            if (dict_t.contains(s[i]))
            {
                filtered_s.push_back({i, s[i]});
            }
        }

        int l = 0;
        int formed = 0;
        unordered_map<char, int> window_counts;

        // 결과 저장할 변수; 길이, 시작인덱스, 골인덱스
        int min_len = INT_MAX;
        int start_idx = 0, end_idx = 0;

        for (int r = 0; r < filtered_s.size(); r++)
        {
            int idx = filtered_s[r].first;
            char ch = filtered_s[r].second;

            window_counts[ch]++;

            if (window_counts[ch] == dict_t[ch]) formed++;

            while (l <= r && formed == required)
            {
                char left_char = filtered_s[l].second;

                int end = filtered_s[r].first;
                int start = filtered_s[l].first;

                if (end - start + 1 < min_len)
                {
                    min_len = end - start + 1;
                    start_idx = start;
                    end_idx = end;
                }

                window_counts[left_char]--;
                if (window_counts[left_char] < dict_t[left_char])
                {
                    formed--;
                }
                l++;
            }
        }

        return min_len == INT_MAX ? "" : s.substr(start_idx, min_len);
    }
};