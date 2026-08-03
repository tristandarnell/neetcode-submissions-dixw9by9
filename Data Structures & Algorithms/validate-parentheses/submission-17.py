class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        check = {"(":")",
        "{":"}", 
        "[":"]"}

        for char in s:
            if char in check:
                stack.append(char)
            else:
                if not stack or check[stack[-1]] != char:
                    return False
                stack.pop()
        return not stack