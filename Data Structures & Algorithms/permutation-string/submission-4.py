class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = len(s1)
        perm = sorted(s1)

        while end < len(s2)+1:
            if perm == sorted(s2[start:end]):
                return True
            start += 1
            end += 1
        return False
