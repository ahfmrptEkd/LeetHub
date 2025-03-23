class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        s 가 t의 한번 건너 뛴 원소에 해당하면; true, 아니면 false
        l 은 s를 나타내고. r 은 t를 나타낸다.
        l += 1 씩 그리고 최소 r += 1 오르면서 다 확인해봐야할듯.

        1. 들어온 s 와 t를 한개씩 나눠 2개의 list에 넣음
        2. 한개에 s만 들어오는게 아니다.
        3. 범위 = len(t)-1
        4. r을 가지고 한다기 보단. l을 이용해 인덱스만 해도 될듯.
        """

        sub = [c for c in s]

        main = [c for c in t]

        l, r = 0, 0

        while l < len(sub) and r < len(main):
            if sub[l] == main[r]:  # s의 현재 원소가 t의 현재 원소와 같으면
                l += 1
                r += 1
            else:
                r += 1  # 같지 않다면, r만 다음칸을 가면서 확인
            
            if r >= len(main) and l < len(sub): # t의 끝까지 도달 했지만, s의 모든 문자를 확인하지 못한 경우.
                return False
        
        return l == len(s)  # s의 모든 문자를 확인한 경우; l == count의 역할을 함. 