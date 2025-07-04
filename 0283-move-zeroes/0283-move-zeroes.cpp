class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] != 0 and nums[slow] == 0) {
                swap(nums[slow], nums[i]);
            }
            if (nums[slow] != 0){
                slow++;
            }
        }
    }
};