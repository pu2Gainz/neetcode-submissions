class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def dfs(i):
        #     if i <= 2:
        #         return i

        #     if i in memo:
        #         return memo[i]
        #     memo[i] = dfs(i - 1) + dfs(i - 2)
        #     return memo[i]
        
        # return dfs(n)
        one, two  = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one