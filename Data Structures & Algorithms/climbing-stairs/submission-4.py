class Solution:
    def climbStairs(self, n: int) -> int:
        cur, prev = 1, 1

        for i in range(2, n + 1):
            temp = cur + prev
            prev = cur 
            cur = temp
        
        return cur