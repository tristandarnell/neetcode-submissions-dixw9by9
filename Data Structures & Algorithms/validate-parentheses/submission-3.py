class Solution:
    def isValid(self, s: str) -> bool:
        keys = {"]" : "[", "}" : "{", ")" : "("}
        stack = []

        for c in s:
            if c in keys:
                if stack and keys[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True
