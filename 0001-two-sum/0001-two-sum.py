class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 한 개의 답이 딱 있다.
        # 같은 원소 2개 안됨
        # dictionary 로 원소의 인덱스 보관
        # 정렬해서 two-pointer 접근
        # target 이 되는 순간 break
        # target 보다 크면 r - 1
        # target 보다 작으면 l + 1
        # 같은 원소에 대해서 i 가 갱신되는거 문제.
        if len(nums) == 2:
            return [0,1]

        l, r = 0, len(nums)-1
        idx = [(v, i) for i, v in enumerate(nums)]
        idx.sort(key=lambda x:x[0])

        while l < r:
            if (idx[l][0] + idx[r][0]) == target:
                return [idx[l][1], idx[r][1]]
            elif (idx[l][0] + idx[r][0]) < target:
                l += 1
            else:
                r -= 1
            