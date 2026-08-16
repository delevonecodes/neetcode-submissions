class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        sent = [ c.lower() for c in s if c.isalnum()]
        l = 0
        r = len(sent) - 1
        while l < r:
            if sent[l] != sent[r]:
                return False
            l += 1
            r -= 1
        return True

