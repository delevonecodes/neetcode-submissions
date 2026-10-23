class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = []
        anagrams = {}
        for string in strs:
            ana = "".join(sorted(string))
            if ana in anagrams:
                anagrams[ana].append(string)
            else:
                anagrams[ana] = [string]

        return [anagram for anagram in anagrams.values()]