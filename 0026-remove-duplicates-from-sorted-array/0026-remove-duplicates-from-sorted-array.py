class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate_checker = [nums[0]]
        change_index = 1

        for i in range(1, len(nums)):
            if nums[i] == duplicate_checker[-1]:
                continue
            else:
                duplicate_checker.append(nums[i])
                nums[change_index] = nums[i]
                change_index += 1
                    
        k = len(duplicate_checker)

        return k