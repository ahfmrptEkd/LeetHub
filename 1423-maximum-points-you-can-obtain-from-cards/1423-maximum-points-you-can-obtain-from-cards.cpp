#include <climits>
#include <numeric>
#include <deque>

using namespace std;

class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int answer = INT_MIN;
        int total_sum = accumulate(cardPoints.begin(), cardPoints.end(), 0);
        
        int window_size = cardPoints.size() - k;  
        
        deque<int> current_window;
        for (int i = 0; i < window_size; i++) 
        {
            current_window.push_back(cardPoints[i]);
        }
        
        int current_sum = accumulate(current_window.begin(), current_window.end(), 0);
        answer = max(answer, total_sum - current_sum);
        
        for (int i = 0; i < k; i++) {
            current_sum -= cardPoints[i];
            current_sum += cardPoints[i + window_size];
            
            answer = max(answer, total_sum - current_sum);
        }
        
        return answer;
    }
};