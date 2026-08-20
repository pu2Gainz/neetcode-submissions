class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # stone[i] is the weight
        # if x < y y = x - y 

        stoneSum = sum(stones)
        target = stoneSum // 2

        dp = [0] * (target + 1)

        for stone in stones:
            for t in range(target, stone - 1, -1):
                dp[t] = max(dp[t], dp[t - stone] + stone)
        






        return stoneSum - 2 * dp[target]