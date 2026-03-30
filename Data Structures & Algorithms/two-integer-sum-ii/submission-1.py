class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) + 1


        while l < r:
            sum = numbers[r] + numbers[l]
            if sum == target:
                return [l, r]
            elif sum > target:
                r -= 1
            elif sum < target:
                l += 1
        return [l, r]


        