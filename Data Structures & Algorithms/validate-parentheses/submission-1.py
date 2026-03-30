class Solution:
    def isValid(self, s: str) -> bool:
        keys = {"[" : "]", "{" : "}", "(" : ")"}
        s = list(s)
        if len(s)%2!=0:
            return False
        for i in range((len(s)//2)):
            print(i)
            if (keys[s[i]] != s[-1]):
                return False
            s.pop()

        return True