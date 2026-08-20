class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        zero = 0
        one = min(cost[0], 0)

        # n = min(cost[n - 2], cost[n - 1]) n is len(cost
        for i in range(2, len(cost) + 1):
            temp = min(zero + cost[i - 2], one + cost[i - 1])
            zero = one
            one = temp
        return one


        # zero: 0, one : 0 two: min(1 + 0, 2 + 0) = 1 three: min(0 + 2, 1 + 3)