class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1)-1
        count_s1, count_s2 = {}, {}
        for char in s1:
            if char in count_s1:
                count_s1[char]+=1
            else:
                count_s1[char]=1
        for i in range(len(s1)):
            if s2[i] in count_s2:
                count_s2[s2[i]]+=1
            else:
                count_s2[s2[i]]=1
        if count_s1 == count_s2:
                return True
        while r < len(s2)-1:
            if count_s1 == count_s2:
                return True
            r+= 1
            if s2[r] in count_s2:
                count_s2[s2[r]] += 1
            else:
                count_s2[s2[r]] = 1
            count_s2[s2[l]]-=1
            if count_s2[s2[l]] == 0:
                count_s2.pop(s2[l], None)
            l+=1
            if count_s1 == count_s2:
                return True
        return False