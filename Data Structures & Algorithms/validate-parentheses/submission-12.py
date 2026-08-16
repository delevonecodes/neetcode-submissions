class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        stack = []
        for char in s:
            if char not in close_to_open:
                stack.append(char)
            elif stack and close_to_open[char] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0

