class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]  # 양쪽에 가상의 0을 추가하여 경계 처리를 간소화
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1  # 꽃을 심음
                count += 1
            if count >= n:
                return True
        return count >= n