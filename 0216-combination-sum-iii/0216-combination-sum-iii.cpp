class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> result;

        queue<tuple<vector<int>, int, int>> q;

        q.push(make_tuple(vector<int>(), 0, 1));

        while(!q.empty()) {
            auto [combination, currentSum, nextNum] = q.front();
            q.pop();

            if (combination.size() == k && currentSum == n) {
                result.emplace_back(combination);
                continue;
            }

            if (combination.size() > k || currentSum > n) {
                continue;
            }

            for (int i = nextNum; i < 10; i++) {
                std::vector<int> newCombination = combination;
                newCombination.push_back(i);
                
                int newSum = currentSum + i;
                
                q.push(std::make_tuple(newCombination, newSum, i + 1));
            }
        }

        return result;
    }
};