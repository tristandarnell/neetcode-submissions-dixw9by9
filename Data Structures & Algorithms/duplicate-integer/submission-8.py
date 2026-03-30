class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains_duplicate = set()

        for num in nums:
            if num in contains_duplicate:
                return True
            contains_duplicate.add(num)
        return False