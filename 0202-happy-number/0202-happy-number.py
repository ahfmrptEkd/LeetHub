class Solution:
    def isHappy(self, n: int) -> bool:
        # 숫자를 다 분해한 뒤, 제곱
        # 제곱한 값을 더함 => output
        # 반복한다. 1이 될때 까지 또는 무한히
        # 실제 반복은 아웃풋을 보고 판단.   dictionary에 같은 숫자가 나오면 루프라고 판단

        # num: 현재 검사 중인 숫자를 리스트로 저장 (길이는 항상 1)
        num = [n]
        # container: 이전에 나왔던 숫자들을 저장하는 set (무한 루프 감지용)
        container = set()
        container.add(n)  # 초기 숫자 추가
        happy = False     # 해피 넘버 여부를 저장할 플래그

        while not happy:
            # 현재 숫자의 각 자릿수를 분리하여 제곱한 후 합산
            # 예: 19 -> '19' -> ('1','9') -> 1²+9² = 82
            output = sum(int(digit)**2 for digit in str(num[0]))
            
            num.pop()          # 이전 숫자 제거
            num.append(output) # 새로 계산된 숫자 추가

            if output == 1:
                return True   # 1이 나오면 해피 넘버
            elif output in container:
                return False   # 이전에 나왔던 숫자가 다시 나오면 무한 루프
            else:
                container.add(output)  # 새로운 숫자를 set에 추가