class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        frequency = defaultdict(int)
        
        for num in nums:
            frequency[num] += 1

        for num, count in frequency.items():
            heapq.heappush(heap, (count, num))
            while len(heap) > k:
                heapq.heappop(heap)

        return [num for count,num in heap]

        