class Solution {
public:
    string decodeString(string s) {
        stack<char> st;

        for(char c : s)
        {
            if (c == ']')
            {
                string decoded = "";

                // 인코딩 추출
                while(!st.empty() && st.top() != '[')
                {
                    decoded = st.top() + decoded;
                    st.pop();
                }
                st.pop(); // '[' 제거

                // 숫자
                int base = 1;
                int k = 0;

                while ( !st.empty() && isdigit(st.top()))
                {
                    k = k + (st.top() - '0') * base;
                    st.pop();
                    base *= 10;
                }

                // 디코딩된 문자열 k번 반복
                string multiple = "";
                for (int i = 0; i < k; i++)
                {
                    multiple += decoded;
                }

                // 결과 다시 스택에 push
                for(char l : multiple)
                {
                    st.push(l);
                }
            }
            else
            {
                st.push(c);
            }
        }

        string result = "";
        while(!st.empty())
        {
            result = st.top() + result;
            st.pop();
        }
        return result;
    }
};