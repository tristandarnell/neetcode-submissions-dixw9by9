class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while True:
            mid = (l + r) // 2

            if target > mid:
                r = mid
            if target < mid:
                l = mid
            if target == mid:
                return mid

        return -1

