#include <ranges>

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        if (s.length() < p.length()) return result;
        
        unordered_map<char, int> dict_p;
        for (char c : p) {
            dict_p[c]++;
        }
        int required = dict_p.size();
        
        int l = 0, formed = 0;
        unordered_map<char, int> window;
        
        for (int r = 0; r < s.length(); r++) {
            char ch = s[r];
            window[ch]++;
            
            // update formed
            if (dict_p.count(ch) && window[ch] == dict_p[ch]) {
                formed++;
            }
            
            // maintain a window size as much as p.length()
            while (r - l + 1 > p.length()) {
                char left_char = s[l];
                if (dict_p.count(left_char) && window[left_char] == dict_p[left_char]) {
                    formed--;
                }
                window[left_char]--;
                l++;
            }
            
            // check anagram 
            if (r - l + 1 == p.length() && formed == required) {
                result.push_back(l);
            }
        }
        
        return result;
    }
};