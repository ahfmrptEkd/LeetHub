from collections import OrderedDict

class LRUCache:
   """
   LRU(Least Recently Used) 캐시를 구현한 클래스
   OrderedDict를 사용하여 삽입 순서를 유지하고 관리합니다.
   
   Attributes:
       capacity (int): 캐시의 최대 용량
       cache (OrderedDict): 키-값 쌍을 저장하는 OrderedDict 객체
   """

   def __init__(self, capacity: int):
       """
       LRUCache 초기화
       Args:
           capacity: 캐시의 최대 용량
       """
       self.capacity = capacity
       self.cache = OrderedDict()

   def get(self, key: int) -> int:
       """
       주어진 키에 해당하는 값을 반환하고, 해당 항목을 최근 사용됨으로 표시
       
       Args:
           key: 찾고자 하는 키
           
       Returns:
           키가 존재하면 해당 값, 없으면 -1
       """
       # 키가 없으면 -1 반환
       if key not in self.cache:
           return -1
       
       # 키가 있으면 해당 항목을 최근 사용됨으로 표시(맨 뒤로 이동)
       self.cache.move_to_end(key)
       return self.cache[key]

   def put(self, key: int, value: int) -> None:
       """
       키-값 쌍을 캐시에 삽입 또는 갱신
       
       Args:
           key: 삽입/갱신할 키
           value: 삽입/갱신할 값
           
       Note:
           - 이미 존재하는 키면 값을 갱신하고 최근 사용됨으로 표시
           - 용량 초과시 가장 오래된 항목(맨 앞) 제거
       """
       # 키가 이미 있으면 최근 사용됨으로 표시
       if key in self.cache:
           self.cache.move_to_end(key)
       # 새로운 키-값 쌍 삽입
       self.cache[key] = value
       # 용량 초과시 가장 오래된 항목 제거
       if len(self.cache) > self.capacity:
           self.cache.popitem(last=False)  # last=False로 첫 번째(가장 오래된) 항목 제거

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)