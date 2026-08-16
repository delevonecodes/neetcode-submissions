class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 1:
            return [[""]]
        hashmap = {}
        for word in strs:
            current_anagram = "".join(sorted(word))
            if current_anagram not in hashmap:
                hashmap[current_anagram] = [word]
            else:
                hashmap[current_anagram].append(word)

        return [group for group in hashmap.values()]