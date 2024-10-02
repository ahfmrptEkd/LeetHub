class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 모든 아이들은 최소 한개의 캔디를 가짐.
        # 더 큰 숫자를 가진 아이는 주변 아이들 보다 더 많이 사탕을 가진다. -> 위치 인덱스는 중요.
        # 최소한으로 캔디를 아낄 수 있는 방법

        given = [1] * len(ratings) 

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                given[i] = given[i-1] + 1

        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                given[j] = max(given[j+1] + 1, given[j])
        
        return sum(given)
    