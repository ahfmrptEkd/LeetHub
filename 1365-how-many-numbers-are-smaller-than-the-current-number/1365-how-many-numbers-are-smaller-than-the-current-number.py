class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count = dict()

        for i, num in enumerate(sorted_nums):
            if num in count:
                continue
            if not num in count:
                count[num] = i

        result = []
        for num in nums:
            result.append(count[num])

        return result