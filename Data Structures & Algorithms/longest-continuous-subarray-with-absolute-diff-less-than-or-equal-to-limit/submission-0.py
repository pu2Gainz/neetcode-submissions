class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxHeap = []
        minHeap = []
        j = 0
        res = 0

        for i, v in enumerate(nums):
            heapq.heappush(maxHeap, (-v, i))
            heapq.heappush(minHeap, (v, i))

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                j += 1
                while maxHeap and maxHeap[0][1] < j:
                    heapq.heappop(maxHeap)

                while minHeap and minHeap[0][1] < j:
                    heapq.heappop(minHeap)

            res = max(res, i - j + 1)

        return res       