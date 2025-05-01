public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        // C#에서는 priority queue를 이용해서 표현
        PriorityQueue<int, int> pq = new PriorityQueue<int, int>();

        // 최대 힙처럼 작동하도록 음수로 설정
        // 시간 복잡도: O(n log n)
        foreach (int num in nums) {
            pq.Enqueue(num, -num);
        }

        // k-1번 pop 수행: O(k log n)
        for (int i = 0; i < k - 1; i++) {
            pq.Dequeue();
        }

        return pq.Dequeue();

    }
}