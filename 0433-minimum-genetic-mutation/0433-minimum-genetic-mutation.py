class Solution:
    def check_one_mutate(self, gen_a, gen_b):
        counter = 0

        for a, b in zip(gen_a, gen_b):
            if a != b:
                counter += 1

        return True if counter == 1 else False


    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank: return -1

        nodes = bank + [startGene]
        graph = collections.defaultdict(list)

        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if self.check_one_mutate(nodes[i], nodes[j]):
                    graph[nodes[i]].append(nodes[j])
                    graph[nodes[j]].append(nodes[i])

        
        queue = collections.deque([[startGene, 0]])
        visited = set()

        while queue:
            current, m_count = queue.popleft()

            if current == endGene: return m_count

            if current in visited: continue

            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append([neighbor, m_count+1])

        return -1