class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        minHeap = []
        for num in count_map.keys():
            heapq.heappush(minHeap, (-count_map[num], num))

        res = []
        while k > 0:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1

        return res

        