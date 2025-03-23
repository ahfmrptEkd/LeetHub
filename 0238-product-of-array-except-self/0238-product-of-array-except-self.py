class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        O(n)으로 풀어야함.
        """
        length = len(nums)

        # 초기화
        l, r, answer = [0] * length, [0] * length, [0] * length

        # l과 r 둘다 하나씩 적게 하여 자기자신을 계산안하게 함.
        l[0] = 1
        for i in range(1, length): 
            l[i] = nums[i-1] * l[i-1]

        
        r[length-1] = 1
        for i in reversed(range(length-1)):
            r[i] = nums[i+1] * r[i+1]
        

        for i in range(length):
            answer[i] = l[i] * r[i]
        
        return answer