class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        l = 0
        last_seen = {}

        for r, char in enumerate(s):
            if char in last_seen and last_seen[char] >= l:
                l = last_seen[char] + 1
            last_seen[char] = r
            max_sub = max(max_sub, r - l + 1)
        return max_sub
            
            

            

