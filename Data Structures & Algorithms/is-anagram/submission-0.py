class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charcount1 = defaultdict(int)
        charcount2 = defaultdict(int)

        for char1 in s:
                charcount1[char1] += 1

        for char2 in t:
                charcount2[char2] += 1

        return charcount1 == charcount2


       