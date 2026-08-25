class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        prefixSum = 0
        res = 0
        for num in nums:
            prefixSum += num
            res += freq[prefixSum - k]
            freq[prefixSum] += 1

        
        return res
            
