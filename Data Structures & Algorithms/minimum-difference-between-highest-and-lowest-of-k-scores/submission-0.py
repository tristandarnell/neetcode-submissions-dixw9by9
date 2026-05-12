class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        score = float('inf')

        for right in range(len(nums)):
            if (right - left + 1) == k:
                highest = nums[right]
                lowest = nums[left]
                score = min(score, highest - lowest)
                left += 1
        return score

        


        