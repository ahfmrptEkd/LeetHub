class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq as hp

        # 현재 자본이 모든 프로젝트의 필요 자본보다 크다면, 가장 큰 k개의 profit만 선택하면 됨
        if w >= max(capital):
            return w + sum(hp.nlargest(k, profits)) # O(n log k)

        # projects를 리스트로 만들고 한번에 heapify: O(n)
        projects = [(c, p) for c, p in zip(capital, profits)]
        hp.heapify(projects)  # O(n)으로 MinHeap 생성
        
        available = []  # MaxHeap
        for _ in range(k):
            # 현재 자본으로 가능한 프로젝트들을 MaxHeap으로
            while projects and projects[0][0] <= w:       # O(n)
                cap, pro = hp.heappop(projects)           # O(log n)
                hp.heappush(available, (-pro, cap))       # O(log n)
            
            if not available:
                break
                
            profit, _ = hp.heappop(available) # O(log n)
            w += -profit
            
        return w