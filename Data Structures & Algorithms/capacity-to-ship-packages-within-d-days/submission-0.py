class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l < r: 
            m = l + (r - l ) // 2
            d = 1
            c = m
            for weight in weights:
                if c >= weight:
                    c -= weight
                else:
                    c = m - weight
                    d += 1

            if d <= days:
                res = m
                r = m
            else:
                l = m + 1

        return res

