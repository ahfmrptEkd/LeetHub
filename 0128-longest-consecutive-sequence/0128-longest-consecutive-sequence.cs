public class Solution {
    public int LongestConsecutive(int[] nums) {
        int streak = 0;
        HashSet<int> dictNum = new HashSet<int>(nums);
        
        foreach (int n in dictNum) {
            if (!dictNum.Contains(n - 1)) {
                int current = n;
                int currentStreak = 1;
                
                while (dictNum.Contains(current + 1)) {
                    current += 1;
                    currentStreak += 1;
                }
                
                streak = Math.Max(streak, currentStreak);
            }
        }
        
        return streak;
    }
}