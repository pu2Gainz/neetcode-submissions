class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            heapq.heappush(minHeap, (x ** 2 + y ** 2, [x, y]))

        res = []
        while k > 0:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1

        return res