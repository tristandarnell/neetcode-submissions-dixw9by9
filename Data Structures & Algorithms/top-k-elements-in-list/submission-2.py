from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_counter = defaultdict(int)
        ans = []

        for num in nums:
            top_counter[num] += 1
        
        for _ in range(k):
            max_key = max(top_counter, key=top_counter.get)
            ans.append(max_key)
            del top_counter[max_key]
        return ans
            
        
        

