class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "]": "[",
            ")": "(",
            "}": "{",
        }
        stack = []
        for c in s:
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            elif stack and parentheses[c] == stack[-1]:
                stack.pop()
            else:
                if not stack or stack[-1] != parentheses[c]:
                    return False
                stack.pop()

        return not stack
