class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            counter[char] += 1
        for char in t:
            counter[char] -= 1
        
        for val in counter.values():
            if val != 0:
                return False
        return True
        