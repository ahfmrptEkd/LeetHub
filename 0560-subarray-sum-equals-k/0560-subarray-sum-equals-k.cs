public class Solution {
    public int SubarraySum(int[] nums, int k) {
        int count = 0;
        int prefixSum = 0;

        var sumCount = new Dictionary<int, int>();
        sumCount[0] = 1;

        foreach (int n in nums)
        {
            prefixSum += n;

            if (sumCount.ContainsKey(prefixSum - k))
            {
                count += sumCount[prefixSum - k];
            }

            if (sumCount.ContainsKey(prefixSum)) sumCount[prefixSum]++;
            else sumCount[prefixSum] = 1;
        }
        return count;
    }
    
}