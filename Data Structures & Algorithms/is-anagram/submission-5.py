from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for char in s:
            count[char] += 1
        for char in t:
            count[char] -= 1
        
        for value in count.values():
            if value != 0:
                return False
        return True
        





