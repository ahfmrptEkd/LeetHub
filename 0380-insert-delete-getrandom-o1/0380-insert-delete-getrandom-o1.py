import random

class RandomizedSet:

    def __init__(self):
        # 상수 시간을 갖기 위해선 hashmap 구현 -> dictionary 이용
        # 인덱싱만을 이용해서 상수시간을 갖춘다.
        self.values = []    # 값을 저장하는 리스트
        self.value_to_index = {}    # 값의 인덱스를 저장하는 딕셔너리

    def insert(self, val: int) -> bool:
        if val not in self.value_to_index:
            self.values.append(val)
            self.value_to_index[val] = len(self.values) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.value_to_index:
            # 삭제할 원소와 마지막 원소의 위치 교환
            last_element = self.values[-1]
            index_to_remove = self.value_to_index[val]
            self.values[index_to_remove] = last_element
            self.value_to_index[last_element] = index_to_remove
            self.values.pop()
            del self.value_to_index[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()