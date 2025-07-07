class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() <= 2) return 0;

        long long answer = 0;
        int n = height.size();

        int l = 0;        
        int r = n - 1;   

        int lmax = height[0];
        int rmax = height[n-1];

        while (l < r)     
        {
            if (lmax <= rmax)
            {
                l++;
                if (height[l] > lmax) {
                    lmax = height[l];
                } else {
                    answer += lmax - height[l];
                }
            }
            else
            {
                r--;
                if (height[r] > rmax) {
                    rmax = height[r];
                } else {
                    answer += rmax - height[r];
                }
            }
        }

        return answer;
    }
};