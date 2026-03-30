from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        ans = []

        for num in nums:
            count[num] += 1

        for _ in range(k):
            top_k = max(count, key=count.get)
            ans.append(top_k)
            del count[top_k]
        
        return ans


            




        