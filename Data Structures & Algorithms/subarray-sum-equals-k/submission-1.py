class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        freq = defaultdict(int)
        freq[0] = 1
        curSum = 0
        res = 0
        for num in nums:
            curSum += num
            res += freq[curSum - k]
            freq[curSum] += 1

        return res

        # 2 -1 1 2
        # 2 curSum = 2 res =
        
