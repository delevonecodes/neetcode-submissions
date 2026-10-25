class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        count = {}
        l, r = 0, 0
        max_freq = 0
        longest = 0
        while r < len(s):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            max_freq = max(count.values())
            distance = (r-l) + 1
            if (distance) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            window = (r-l) + 1
            longest = max(longest, window)
            r += 1
        return longest



            