class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) <= 2:    # safe coding
            return 0

        ans = 0

        l = 1
        r = len(height)-1

        lmax = height[0]
        rmax = height[-1]

        while l <= r:

            if height[l] > lmax:
                lmax = height[l]
            if height[r] > rmax:
                rmax = height[r]
        

            if lmax <= rmax:
                ans += lmax - height[l]
                l += 1
            else:
                ans += rmax-height[r]
                r -= 1
        
        return ans