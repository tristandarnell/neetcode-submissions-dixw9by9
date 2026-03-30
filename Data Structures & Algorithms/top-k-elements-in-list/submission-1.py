from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []

        for _ in range(k):
            k_times = max(count, key=count.get)
            ans.append(k_times)
            del count[k_times]
        return ans
             

