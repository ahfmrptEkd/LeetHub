class Solution {
public:
    vector<int> partitionLabels(string s) {
        // 1. save each char's last index
        unordered_map<char, int> lastIndex;
        for (int i = 0; i < s.length(); i++)
        {
            lastIndex[s[i]] = i;
        }

        vector<int> result;
        int start = 0;
        int end = 0;

        // 2. split string by one-pass
        for (int i = 0; i < s.length(); i++)
        {
            // update end to current char's last index position
            end = max(end, lastIndex[s[i]]);

            if (i == end)
            {
                result.push_back(end - start + 1);
                start = i + 1;
            }
            
        }

        return result;
    }
};