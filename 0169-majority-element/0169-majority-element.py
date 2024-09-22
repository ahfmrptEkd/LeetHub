class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        most bin 은 n/2 만큼
        n^2 까진 한도
        정렬 후 그 빈도수 체크로 나아가면 될 듯
        max 값을 유지하면서 가는 것.(value, 빈도)
        """
        max_bin = dict()

        for i, k in enumerate(nums):
            if k in max_bin:
                max_bin[k] += 1
            else:
                max_bin[k] = 1
        
        ans = max(max_bin, key=max_bin.get)
        return ans


        