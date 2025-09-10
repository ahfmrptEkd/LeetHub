public class MedianFinder {
    private PriorityQueue<int, int> small;
    private PriorityQueue<int, int> big;


    public MedianFinder() {
        small = new PriorityQueue<int, int>(Comparer<int>.Create((x, y) => y.CompareTo(x))); // max heap
        big = new PriorityQueue<int, int>(); // min heap
    }
    
    public void AddNum(int num) {
        if (small.Count == big.Count)
        {
            big.Enqueue(num, num);
            small.Enqueue(big.Peek(), big.Peek());
            big.Dequeue();
        }
        else
        {
            small.Enqueue(num, num);
            big.Enqueue(small.Peek(), small.Peek());
            small.Dequeue();
        }
    }
    
    public double FindMedian() {
        if (small.Count == 0) return 0;
        if (small.Count > big.Count) return small.Peek();
        return (small.Peek() + big.Peek()) / 2.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.AddNum(num);
 * double param_2 = obj.FindMedian();
 */