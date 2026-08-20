class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for stone in stones:
            heapq.heappush(minHeap, -stone)
        
        while len(minHeap) > 1:
            stone1 = heapq.heappop(minHeap)
            stone2 = heapq.heappop(minHeap)

            if stone1 == stone2:
                continue
            else:
                heapq.heappush(minHeap, -abs(stone1 - stone2))

        return 0 if not minHeap else -minHeap[0]
        