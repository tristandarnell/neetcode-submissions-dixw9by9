from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        ans = []
        counts = dict(sorted(counts.items(), key=lambda i : i[1], reverse=True))
        for key, value in counts.items():
            if k > 0:
                ans.append(key)
            else:
                break
            k -= 1
        return ans