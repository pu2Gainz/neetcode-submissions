class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        
        while l < r:
            mid = l + (r - l) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / mid)
            
            if hour > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid
        return res