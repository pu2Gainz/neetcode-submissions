class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob1, rob2 = 0, 0
        r1, r2 = 0, 0
        if n < 2: 
            return nums[0]
        for i in nums[0: n - 1]:
            temp = max(rob1 + i, rob2)
            rob1= rob2
            rob2 = temp

        for i in nums[1: n]:
            temp = max(r1 + i, r2)
            r1= r2
            r2 = temp
        
        return max(rob2, r2)