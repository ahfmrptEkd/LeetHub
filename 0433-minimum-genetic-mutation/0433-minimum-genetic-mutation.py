class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        def gene_checker(gene):
            # 가능한 모든 유전자 문자
            genes = ['A','C','G','T']
            possible = []
            # 문자열을 리스트로 변환 (문자열은 불변이라 수정 불가)
            curr_list = list(gene)
            
            # 각 위치(8개)에 대해 가능한 모든 돌연변이 확인
            for i in range(8):
                original = curr_list[i]  # 현재 위치의 원래 문자 저장
                for g in genes:
                    # 현재 문자와 다른 경우만 시도
                    if g != original:
                        curr_list[i] = g
                        new_gene = "".join(curr_list)
                        # bank에 있는 유효한 유전자인 경우만 추가
                        if new_gene in bank:
                            possible.append(new_gene)
                curr_list[i] = original  # 원래 문자로 복구
            return possible

        # BFS를 위한 큐 초기화 (시작 유전자와 돌연변이 횟수)
        queue = deque([(startGene, 0)])
        visited = set()  # 방문한 유전자 문자열 저장

        # BFS 수행
        while queue:
            gen, mutate = queue.popleft()

            # 목표 유전자에 도달한 경우
            if gen == endGene:
                return mutate

            # 현재 유전자에서 가능한 모든 다음 유전자 확인
            genes = gene_checker(gen)

            # 방문하지 않은 새로운 유전자에 대해 큐에 추가
            for gene in genes:
                if gene not in visited:
                    visited.add(gene)
                    queue.append((gene, mutate+1))

        # 목표 유전자에 도달할 수 없는 경우
        return -1