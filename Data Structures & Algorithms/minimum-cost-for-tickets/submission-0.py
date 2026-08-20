class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 1, 7, 30 weight
        # prfit cost[i]
        # capacity: len(days) days is sorted 

       
        dp = [0] * 366
        i = 0

        for d in range(1, 366):
            dp[d] = dp[d - 1]
            if i == len(days):
                return dp[d]

            if d == days[i]:
                dp[d] += costs[0]
                dp[d] = min(dp[d], costs[1] + dp[max(0, d - 7)])
                dp[d] = min(dp[d], costs[2] + dp[max(0, d - 30)])
                i += 1

        return dp[365]

            

