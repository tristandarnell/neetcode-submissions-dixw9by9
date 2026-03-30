class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right = left = swaps = ans = 0
        count = 0
        while right < len(s):
            if s[left] == s[right]:
                count+=1
            elif s[left] != s[right]:
                swaps += 1
            while swaps > k:
                left = right
                swaps = 0
                count = 1
            
            ans = max(ans, right - left + 1)
            right += 1
        return ans