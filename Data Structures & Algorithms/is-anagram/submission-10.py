class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        valid = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            valid[char] += 1
        
        for char in t:
            valid[char] -= 1
            if valid[char] < 0:
                return False
        return True

        