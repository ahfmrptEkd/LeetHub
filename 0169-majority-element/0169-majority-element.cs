public class Solution {
    public int MajorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;

        foreach (int num in nums){
            if (count == 0) {
                candidate = num;
            }
            _ = (num == candidate) ? count++ : count--;
        }

        return candidate;
    }
}