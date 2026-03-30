class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, curr, value):
            if value == target:
                res.append(curr[:])
                return
            elif value > target or idx >= len(nums):
                return
            
            curr.append(nums[idx])
            dfs(idx, curr, value+nums[idx])
            curr.pop()
            dfs(idx+1, curr, value)

        dfs(0, [], 0)
        return res