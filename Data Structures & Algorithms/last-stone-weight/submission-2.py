import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1
            val = abs(x-y)
            if val > 0:
                heapq.heappush(heap, val*-1)
        
        return heap[0]*-1 if len(heap) > 0 else 0
        