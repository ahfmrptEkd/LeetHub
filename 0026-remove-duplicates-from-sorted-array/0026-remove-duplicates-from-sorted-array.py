class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1

        for i in range(len(nums)-1):
            # print(nums[l], nums[r-1])

            if r >= len(nums) or (nums[l] == nums[r]):   # 범위 제한
                nums.pop(r)
            else:
                l += 1
                r = l + 1
