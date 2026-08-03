class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        left = 0
        longest = 0
        count = 0

        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left])
                left += 1
            else:
                check.add(s[right])
                count += 1
            longest = max(longest, ((right - left) + 1))
        return longest

            



        