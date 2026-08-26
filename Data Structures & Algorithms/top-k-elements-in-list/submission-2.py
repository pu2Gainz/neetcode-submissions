class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqM = Counter(nums)
        maxHeap = []
        for num, freq in freqM.items():
            heapq.heappush(maxHeap, [-freq, num])

        res = []
        while k > 0:
            freq, num = heapq.heappop(maxHeap)
            res.append(num)
            k -= 1
        
        return res