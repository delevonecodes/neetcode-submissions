class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            length = str(len(word))
            code += length+"#"+word
        return code
         

    def decode(self, s: str) -> List[str]:
        strs = []
        y = 0
        while y < len(s):
            j = y
            while s[j] !="#":
                j+=1
            length = int(s[y:j])
            strs.append(s[j+ 1: j + 1 + length])   
            y = j+ 1 + length
        return strs