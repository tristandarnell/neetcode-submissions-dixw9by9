class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())

        left, right = 0, len(cleaned) - 1

        while right > left:
            if cleaned[right] == cleaned[left]:
                right -= 1
                left += 1
            else:
                return False
        return True