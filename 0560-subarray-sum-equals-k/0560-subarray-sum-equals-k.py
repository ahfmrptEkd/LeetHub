class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_count = {0 : 1} # initial for "0" sum occured "1" time.

        for n in nums:
            prefix_sum += n

            # prefix - k exist in sum_dict?
                # same value is existing in dict
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]

            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        return count