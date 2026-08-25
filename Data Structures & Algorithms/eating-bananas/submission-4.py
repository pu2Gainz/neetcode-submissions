class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r: 
            m = l + (r - l) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / m)
            
            if hour <= h: 
                res = m
                r = m - 1
            else:
                l = m + 1
         
        return res

