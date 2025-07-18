class Solution {
public:
    bool isValid(string s) {
        if (s.length() == 1) return false;

        stack<char> stack;
        unordered_map<char, char> map = {
                                            {')', '('},
                                            {'}', '{'},
                                            {']', '['}
                                        };

        for (char c : s)
        {
            if (stack.empty()) stack.push(c);
            
            else if (!map.contains(c)) stack.push(c);

            else
            {
                if (map[c] == stack.top()) stack.pop();

                else return false;
            } 
        }

        return stack.empty();
    }
};