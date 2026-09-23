class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in find_map:
                return [find_map[complement], i]
            find_map[num] = i
            