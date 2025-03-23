class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 논문의 인용 회수 이하인 최대값 찾는 문제.
        citations.sort(reverse=True)
        h_index = 0
        
        for i, cite in enumerate(citations):
            rank = i + 1    # rank = 1 부터 시작 큰 문서는 최소 한번이상 인용 

            if cite >= rank:
                h_index = rank 
            else:
                break

        return h_index