from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        required = len(dict_t)

        # Filter s to include only the characters in t
        filtered_s = [(i, char) for i, char in enumerate(s) if char in dict_t]

        l = 0
        formed = 0
        window_counts = Counter()
        ans = float("inf"), None, None

        for r, (index, char) in enumerate(filtered_s):
            window_counts[char] += 1

            if window_counts[char] == dict_t[char]:
                formed += 1

            while l <= r and formed == required:
                char = filtered_s[l][1]

                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[char] -= 1
                if window_counts[char] < dict_t[char]:
                    formed -= 1
                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]