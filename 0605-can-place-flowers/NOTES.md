```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:​        
        indexes = [index for index, element in enumerate(flowerbed) if element == 0]    # 1,2,3
        cnt = 0
        
        # # 씨앗이 없는 경우 (1)
        if n == 0: return True

        # # 화분이 한개인 경우에 대한 세이프 코딩 (2)
        if len(flowerbed) == 1 and flowerbed[0] == 1: return False
        if len(flowerbed) == 1: return True

        # # 기존 경우
        for i in range(n):  # n=2 2번 만큼
            for j in indexes: # 3번 -> 1,2,3
                
                # 리스트의 범위를 벗어나지 않는지 확인
                if j == 0 and flowerbed[j+1] !=1 and flowerbed[j] != 1:                   # 첫 원소가 0인 경우 대한 세이프 코드
                    flowerbed[j] = 1
                    cnt += 1
                    break

                elif j == len(flowerbed)-1 and flowerbed[j-1] != 1 and flowerbed[j] != 1:   # 마지막 행에 대한 세이프 코드
                    flowerbed[j] = 1
                    cnt += 1
                    break
                elif (j == 0 or flowerbed[j-1] == 1) or (j == len(flowerbed)-1 or flowerbed[j+1] == 1):                
                    continue
                
                elif flowerbed[j] == 1:
                    continue
                
                else:
                    flowerbed[j] = 1
                    cnt += 1
                    break

        return cnt == n
```
이 코드는 내 첫 시행 코드로 시간복잡도는 O(N*M)이지만, 씨앗의 개수와 화분의 길이가 커질 수 록 비효율적인 코드가 된다.  

개선하여 통과한 코드는 앞 뒤로 가상의 0 을 만들어 씨앗의 가능 여부만 따진다. 그래서 count 는 최소 N보다 크거나 같게 된다.
시간복잡도는 O(M) 으로 완전 탐색으로 풀 수 있다.
    
