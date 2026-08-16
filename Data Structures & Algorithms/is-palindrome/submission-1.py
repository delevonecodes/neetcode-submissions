class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        word = [c.lower() for c in s if c.isalnum()]
        
        front = 0
        back = -1
        for i in range(len(word)//2):
            if word[front] != word[back]:
                return False
            front += 1
            back -= 1

        return True