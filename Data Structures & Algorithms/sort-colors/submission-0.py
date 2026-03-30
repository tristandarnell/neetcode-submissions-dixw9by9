class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1
        
        index = 0

        for value in range(3):
            while count[value] > 0:
                nums[index] = value
                index += 1
                count[value] -= 1
        