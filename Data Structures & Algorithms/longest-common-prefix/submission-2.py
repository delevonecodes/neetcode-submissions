class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        smallest = strs[0]
        for string in strs:
            if len(string) < len(smallest):
                smallest = string

        for i in range(len(smallest)):
            for string in strs:
                if string[i] != smallest[i]:
                    return prefix
            prefix += smallest[i]
        return prefix
