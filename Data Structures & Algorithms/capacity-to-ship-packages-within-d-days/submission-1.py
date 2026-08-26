class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        while l < r:
            mid = l + (r - l) // 2
            d = 1
            c = mid
            for weight in weights:
                if c < weight: 
                    d += 1
                    c = mid
                if c >= weight:
                    c -= weight
            
            print(d, mid)
            
            if d > days:
                l = mid + 1
            else: 
                res = min(res, mid)
                r = mid

        return res