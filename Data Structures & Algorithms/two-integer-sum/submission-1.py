class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap1 = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap1:
                return [hashmap1[complement], i]
            hashmap1[num] = i
            