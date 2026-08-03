class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1
            window_size = (right - left + 1)

            while window_size - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
                window_size = (right - left + 1)
        
            res = max(res, window_size)
        return res







        


        