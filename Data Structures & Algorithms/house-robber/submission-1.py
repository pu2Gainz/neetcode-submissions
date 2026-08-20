class Solution:
    def rob(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        
        # if len(nums) == 1:
        #     return nums[0]

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # return dp[-1]


        rob1 = 0 
        rob2 = 0

        for num in nums:
            temp = rob2
            rob2 = max(rob2, rob1 + num)
            rob1 = temp
        
        return rob2