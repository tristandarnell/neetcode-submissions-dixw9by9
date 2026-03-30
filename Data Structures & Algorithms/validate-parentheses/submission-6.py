class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {')':'(', 
        ']':'[', 
        '}':'{'}
        for i in s:
            if i in maps:
                if stack and maps[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True