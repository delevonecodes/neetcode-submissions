class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        ans = {}
        for s in strs:
            sorted_word = "".join(sorted(list(s)))
            if sorted_word in ans:
                ans[sorted_word].append(s)
            else:
                ans[sorted_word] = [s]

        for anagrams in ans.values():
            out.append(anagrams)

        return out