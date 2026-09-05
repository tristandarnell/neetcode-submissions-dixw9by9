class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            heapq.heappush(heap, (count,num))

        while len(heap) > k:
            heapq.heappop(heap)
        
        return [num for (count, num) in heap]
