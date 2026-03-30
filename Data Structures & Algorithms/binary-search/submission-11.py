class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[target] == target:
                r = mid
            elif nums[mid] < target:
                l = mid
            else:
                return mid

        return -1

