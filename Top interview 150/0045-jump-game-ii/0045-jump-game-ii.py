class Solution:
    def jump(self, nums: List[int]) -> int:
        # 무조건 가능 전제
        # 최솟값 찾는 거 같음
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_jump_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i]) # i + j 최대 점프 거리

            if i == current_jump_end:   # 인덱스가 내가 다시 점프할 입장까지 따라 옴
                jumps += 1
                current_jump_end = farthest

                if current_jump_end >= len(nums)-1:
                    break

        return jumps