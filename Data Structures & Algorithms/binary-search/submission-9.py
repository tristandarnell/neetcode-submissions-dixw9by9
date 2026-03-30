class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[target] > nums[mid]:
                r = mid
            if target < mid:
                l = mid
            if nums[target] == target:
                return mid

        return -1

