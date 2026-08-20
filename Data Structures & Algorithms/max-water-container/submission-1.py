class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        amount  = 0

        while l < r:
            amount = max(amount, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        
        return amount